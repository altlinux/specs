%define _unpackaged_files_terminate_build 1
%define bind_version 9.16.34

%define restart_flag /run/named/named.restart

Name: bind-dyndb-ldap
Version: 11.10
Release: alt2

Summary: LDAP back-end plug-in for BIND
License: %gpl2plus
Group: System/Servers

URL: https://pagure.io/bind-dyndb-ldap 
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: bind-devel >= %bind_version
BuildRequires: libldap-devel
BuildRequires: libkrb5-devel
BuildRequires: libuuid-devel
BuildRequires: libsasl2-devel

Requires: bind >= %bind_version

%description
This package provides an LDAP back-end plug-in for BIND. It features
support for dynamic updates and internal caching, to lift the load
off of your LDAP server.

%prep
%setup
%patch -p1

%build
%autoreconf
export BIND9_CFLAGS='-I/usr/include/bind9'
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/bind/zone/dyndb-ldap/

%pre
# upgrade

# Previously, during an upgrade transaction named failed on restart
# with binary incompatible dyndb plugin (not updated yet). So the
# special file-flag is created if named was running before upgrade.
# Later, named's filetrigger checks it for restart.
if [ "$1" -gt 1 ] && [ ! -f '%restart_flag' ]; then
    SYSTEMCTL=systemctl
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" is-active bind.service >/dev/null 2>&1 &&
        "$SYSTEMCTL" stop bind.service 2>/dev/null &&
        mkdir -p "$(dirname '%restart_flag')" &&
        touch '%restart_flag' 2>/dev/null ||:
    else
        %_initdir/bind status >/dev/null 2>&1 &&
        %_initdir/bind stop 2>/dev/null &&
        mkdir -p "$(dirname '%restart_flag')" &&
        touch '%restart_flag' 2>/dev/null ||:
    fi
fi

%post
# The following sed script:
#   - scopes the named.conf changes to dynamic-db
#   - replaces arg "name value" syntax with name "value"
#   - changes dynamic-db header to dyndb
#   - uses the new way the define path to the library
#   - removes no longer supported arguments (library, cache_ttl,
#       psearch, serial_autoincrement, zone_refresh)
while read -r PATTERN
do
    SEDSCRIPT+="$PATTERN"
done <<EOF
/^\s*dynamic-db/,/};/ {

  s/\(\s*\)arg\s\+\(["']\)\([a-zA-Z_]\+\s\)/\1\3\2/g;

  s/^dynamic-db/dyndb/;

  s@\(dyndb "[^"]\+"\)@\1 "%_libdir/bind/ldap.so"@;
  s@\(dyndb '[^']\+'\)@\1 '%_libdir/bind/ldap.so'@;

  /\s*library[^;]\+;/d;
  /\s*cache_ttl[^;]\+;/d;
  /\s*psearch[^;]\+;/d;
  /\s*serial_autoincrement[^;]\+;/d;
  /\s*zone_refresh[^;]\+;/d;
}
EOF

sed -i.bak --follow-symlinks -e "$SEDSCRIPT" /etc/named.conf

%files
%_defaultdocdir/%name
%_libdir/bind/ldap.so
%dir %attr(770, root, named) %_localstatedir/bind/zone/dyndb-ldap/

%exclude %_libdir/bind/*.la

%changelog
* Fri Nov 04 2022 Stanislav Levin <slev@altlinux.org> 11.10-alt2
- Fixed build with Bind 9.16.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 11.10-alt1
- 11.1 -> 11.10.

* Thu Oct 10 2019 Stanislav Levin <slev@altlinux.org> 11.1-alt8
- Added workaround for LDAP socket error on BIND start.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 11.1-alt7
- Fixed upgrade bind 9.9 -> 9.11.

* Fri May 17 2019 Stanislav Levin <slev@altlinux.org> 11.1-alt6
- Applied upstream patch.

* Mon Nov 26 2018 Stanislav Levin <slev@altlinux.org> 11.1-alt5
- Built with new bind 9.11.5.
- Fixed bind-dyndb-ldap upgrade.

* Thu Sep 20 2018 Stanislav Levin <slev@altlinux.org> 11.1-alt4
- Built with new bind 9.11.4.P2.

* Tue Aug 14 2018 Stanislav Levin <slev@altlinux.org> 11.1-alt3
- Rebuild with new bind 9.11.4.P1

* Wed Apr 04 2018 Stanislav Levin <slev@altlinux.org> 11.1-alt2
- Rebuild with new bind 9.11.3

* Tue Nov 07 2017 Stanislav Levin <slev@altlinux.org> 11.1-alt1
- 10.1 -> 11.1

* Wed Aug 02 2017 Dmitry V. Levin <ldv@altlinux.org> 10.1-alt3
- Built with bind-devel-9.10.6.

* Wed Dec 28 2016 Mikhail Efremov <sem@altlinux.org> 10.1-alt2
- Fix spec.
- packaging typos fixed (by Sergey Bolshakov).

* Mon Nov 14 2016 Mikhail Efremov <sem@altlinux.org> 10.1-alt1
- Initial build.

