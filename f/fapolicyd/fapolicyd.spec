%define _localstatedir /var

Name: fapolicyd
Summary: Application Whitelisting Daemon
Version: 1.3.3
Release: alt2
License: GPL-3.0-or-later
Group: System/Base
Url: http://people.redhat.com/sgrubb/fapolicyd
Vcs: https://github.com/linux-application-whitelisting/fapolicyd.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-systemd rpm-macros-python3 rpm-macros-python
BuildRequires: systemd-devel libudev-devel libssl-devel librpm-devel libmagic-devel file
BuildRequires: libcap-ng-devel libseccomp-devel liblmdb-devel
# BuildRequires: python3-devel
BuildRequires: libuthash-devel
# For check
BuildRequires: /proc

%description
Fapolicyd (File Access Policy Daemon) implements application whitelisting
to decide file access rights. Applications that are known via a reputation
source are allowed access while unknown applications are not. The daemon
makes use of the kernel's fanotify interface to determine file access rights.

%prep
%setup
%patch -p1

# generate rules for python
sed -i "s|%%python2_path%%|`readlink -f %__python`|g" rules.d/*.rules
sed -i "s|%%python3_path%%|`readlink -f %__python3`|g" rules.d/*.rules

# Detect run time linker directly from bash
interpret=`readelf -e /bin/bash \
		| grep Requesting \
		| sed 's/.$//' \
		| rev | cut -d" " -f1 \
		| rev`

sed -i "s|%%ld_so_path%%|`realpath $interpret`|g" rules.d/*.rules

%build
%autoreconf
%configure \
    --with-audit \
    --with-rpm \
    --runstatedir=/run

%make_build

%install
%makeinstall_std
mv %buildroot%_datadir/bash-completion/completions/fapolicyd.bash_completion %buildroot%_datadir/bash-completion/completions/%name
install -p -m 644 -D init/%name-tmpfiles.conf %buildroot/%_tmpfilesdir/%name.conf
mkdir -p %buildroot%_localstatedir/lib/%name
mkdir -p %buildroot%_sysconfdir/%name/trust.d
mkdir -p %buildroot%_sysconfdir/%name/rules.d
# get list of file names between known-libs and restrictive from sample-rules/README-rules
cat %buildroot/%_datadir/%name/sample-rules/README-rules \
  | grep -A 100 'known-libs' \
  | grep -B 100 'restrictive' \
  | grep '^[0-9]' > %buildroot%_datadir/%name/default-ruleset.known-libs
chmod 644 %buildroot%_datadir/%name/default-ruleset.known-libs

# ghost files
touch %buildroot%_sysconfdir/%name/{%name,compiled}.rules
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/%name-access.log
touch %buildroot%_localstatedir/lib/%name/{data,lock}.mdb

for file in $(cat %buildroot%_datadir/%name/default-ruleset.known-libs); do
    touch %buildroot%_sysconfdir/%name/rules.d/$file
done

#cleanup
find %buildroot \( -name '*.la' -o -name '*.a' \) -delete

%define manage_default_rules   default_changed=0 \
  # check changed fapolicyd.rules \
  if [ -e %_sysconfdir/%name/%name.rules ]; then \
    diff %_sysconfdir/%name/%name.rules %_datadir/%name/%name.rules.known-libs >/dev/null 2>&1 || { \
      default_changed=1; \
      #echo "change detected in fapolicyd.rules"; \
    } \
  fi \
  if [ -e %_sysconfdir/%name/rules.d ]; then \
    default_ruleset=''; \
    # get listing of default rule files in known-libs \
    [ -e %_datadir/%name/default-ruleset.known-libs ] && default_ruleset=`cat %_datadir/%name/default-ruleset.known-libs`; \
    # check for removed or added files \
    default_count=`echo "$default_ruleset" | wc -l`; \
    current_count=`ls -1 %_sysconfdir/%name/rules.d/*.rules | wc -l`; \
    [ $default_count -eq $current_count ] || { \
      default_changed=1; \
      # echo "change detected in number of rule files d:$default_count vs c:$current_count"; \
    }; \
    for file in %_sysconfdir/%name/rules.d/*.rules; do \
      if echo "$default_ruleset" | grep -q "`basename $file`"; then \
        # compare content of the rule files \
        diff $file %_datadir/%name/sample-rules/`basename $file` >/dev/null 2>&1 || { \
          default_changed=1; \
          # echo "change detected in `basename $file`"; \
        }; \
      else \
        # added file detected \
        default_changed=1; \
        # echo "change detected in added rules file `basename $file`"; \
      fi; \
    done; \
  fi; \
  # remove files if no change against default rules detected \
  [ $default_changed -eq 0 ] && rm -rf %_sysconfdir/%name/%name.rules %_sysconfdir/%name/rules.d/* || : \

%check
make check

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -N -g %name -c 'Application Whitelisting Daemon' \
        -s /sbin/nologin -M -d %_localstatedir/lib/%name %name 2>/dev/null ||:

if [ $1 -eq 2 ]; then
# detect changed default rules in case of upgrade
%manage_default_rules
fi

%post
RESTORECON=/usr/sbin/restorecon
# if no pre-existing rule file
if [ ! -e %_sysconfdir/%name/%name.rules ] ; then
  files=`ls %_sysconfdir/%name/rules.d/ 2>/dev/null | wc -w`
  # Only if no pre-existing component rules
  if [ "$files" -eq 0 ] ; then
    ## Install the known libs policy
    for rulesfile in `cat %_datadir/%name/default-ruleset.known-libs`; do
      cp %_datadir/%name/sample-rules/$rulesfile  %_sysconfdir/%name/rules.d/
    done
    chgrp %name %_sysconfdir/%name/rules.d/*
    if [ -x $RESTORECON ] ; then
      # restore correct label
      $RESTORECON -F %_sysconfdir/%name/rules.d/*
    fi
    fagenrules >/dev/null
  fi
fi
%systemd_post %name.service

%preun
%systemd_preun %name.service
if [ $1 -eq 0 ]; then
# detect changed default rules in case of uninstall
%manage_default_rules
else
  [ -e %_sysconfdir/%name/%name.rules ] && rm -rf %_sysconfdir/%name/rules.d/* || :
fi

%postun
%systemd_postun_with_restart %name.service

%files
%doc README.md COPYING
%_datadir/%name
%attr(750,root,%name) %dir %_sysconfdir/%name
%attr(750,root,%name) %dir %_sysconfdir/%name/trust.d
%attr(750,root,%name) %dir %_sysconfdir/%name/rules.d
%_datadir/bash-completion/completions/%name
%ghost %verify(not md5 size mtime) %attr(644,root,%name) %_sysconfdir/%name/rules.d/*
%ghost %verify(not md5 size mtime) %attr(644,root,%name) %_sysconfdir/%name/%name.rules
%config(noreplace) %attr(644,root,%name) %_sysconfdir/%name/%name.conf
%config(noreplace) %attr(644,root,%name) %_sysconfdir/%name/%name-filter.conf
%config(noreplace) %attr(644,root,%name) %_sysconfdir/%name/%name.trust
%ghost %attr(644,root,%name) %_sysconfdir/%name/compiled.rules
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%_sbindir/%name
%_sbindir/%name-cli
%_sbindir/fagenrules
%_man8dir/*
%_man5dir/*
%ghost %attr(440,%name,%name) %verify(not md5 size mtime) %_logdir/%name-access.log
%attr(770,root,%name) %dir %_localstatedir/lib/%name
%ghost %attr(660,%name,%name) %verify(not md5 size mtime) %_localstatedir/lib/%name/data.mdb
%ghost %attr(660,%name,%name) %verify(not md5 size mtime) %_localstatedir/lib/%name/lock.mdb

%changelog
* Fri Jun 21 2024 Alexey Shabalin <shaba@altlinux.org> 1.3.3-alt2
- Return error code 1 if can't read pid file (ALT#50543).
- Revert "fix default systemd unit dir".

* Fri May 03 2024 Alexey Shabalin <shaba@altlinux.org> 1.3.3-alt1
- New version 1.3.3.

* Mon Sep 18 2023 Alexey Shabalin <shaba@altlinux.org> 1.3.2-alt1
- Initial build.
