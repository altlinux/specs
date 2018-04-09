%define modname mod_auth_token
%define module_name auth_token

Name:    apache2-%modname
Version: 1.0.5
Release: alt1

Summary: Token based URI access module for Apache 2.x
Group:   System/Servers
License: Apache 2.0
URL:     http://code.google.com/p/mod-auth-token/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %modname-%version.tar
Source1: auth_token.load
Source2: auth_token.start

BuildRequires(pre): apache2-devel
BuildRequires: %apache2_apr_buildreq

Requires: apache2 >= %apache2_version-%apache2_release

Provides: %modname = %EVR

%description
mod_auth_token allow you to generate URIS for a determined time window,
you can also limit them by IP. This is very useful to handle file
downloads, generated URIS can't be hot-linked (after it expires), also
it allows you to protect very large files that can't be piped trough a
script languages due to memory limitation.

%prep
%setup -q -n %modname-%version
%autoreconf
%configure --with-apxs=%apache2_apxs \
           --with-apr=%apache2_apr_config

%build
%make_build

%install
install -Dm 644 .libs/%modname.so %buildroot%apache2_libexecdir/%modname.so
install -Dm 644 %SOURCE1 $RPM_BUILD_ROOT%apache2_mods_available/%module_name.load
subst 's,@a_libexecdir@,%apache2_libexecdir,g' $RPM_BUILD_ROOT%apache2_mods_available/%module_name.load
install -Dm 644 %SOURCE2 $RPM_BUILD_ROOT%apache2_mods_start/100-%module_name.conf
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/%module_name.load

%post
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To use %modname check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 %modname module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi


%postun
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
        service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
        echo "To complete %module_name uninstalling check configuration and restart %apache2_dname service."
        echo
    fi
fi

%files
%doc README LICENSE COPYING AUTHORS ChangeLog
%apache2_libexecdir/%modname.so
%config(noreplace) %apache2_mods_available/%module_name.load
%config(noreplace) %apache2_mods_start/100-%module_name.conf
%ghost %apache2_mods_enabled/*.load

%changelog
* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build in Sisyphus

