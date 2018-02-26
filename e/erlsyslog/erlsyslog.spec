%def_with debug
%def_with native

%define svnrev 8
Name: erlsyslog
Version: 0.0
Release: alt0.3
Summary: Syslog facility for Erlang
License: %gpl3plus
Group: Development/Erlang
URL: http://code.google.com/p/%name/
%ifdef svnrev
# svn checkout http://erlsyslog.googlecode.com/svn/trunk/ erlsyslog
Source: %name-svn-r%svnrev.tar
%else
Source: %name-%version.tar
%endif
Requires: erlang-otp-common
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: erlang rpm-build-erlang

%description
Syslog facility for Erlang.


%package -n erlang-%name
Summary: Syslog facility for Erlang
Group: Development/Erlang
BuildArch: noarch
Provides: %name = %version-%release

%description -n erlang-%name
Syslog facility for Erlang.


%if_with debug
%package -n erlang-%name-debug
Summary: Syslog facility for Erlang - module with debug information
Group: Development/Erlang
BuildArch: noarch
Provides: %name-debug = %version-%release

%description -n erlang-%name-debug
Syslog facility for Erlang.
This package contains module with debug information.
%endif


%if_with native
%package -n erlang-%name-native
Summary: Syslog facility for Erlang - module with native CPU code
Group: Development/Erlang
Provides: %name-native = %version-%release

%description -n erlang-%name-native
Syslog facility for Erlang.
This package contains module with native CPU code.
%endif


%package -n erlang-%name-devel
Summary: Header for development with %name
Group: Development/Erlang
BuildArch: noarch
Provides: %name-devel = %version-%release

%description -n erlang-%name-devel
This package contains header for development with %name.


%prep
%setup %{?svnrev:-n %name-svn-r%svnrev}


%build
mkdir ebin
%__erlc %{?eoptflags:%eoptflags} -o ebin %name.erl
%if_with debug
mkdir ebin.debug
%__erlc %{?eoptflags:%eoptflags} +debug_info -o ebin.debug %name.erl
%endif
%if_with native
mkdir ebin.native
%__erlc %{?eoptflags:%eoptflags} +native +'{hipe,[o2]}' -o ebin.native %name.erl
%endif


%install
install -D -m 0644 {,%buildroot%_otplibdir/%name-%version/}ebin/%name.beam
install -D -m 0644 {,%buildroot%_otplibdir/%name-%version/include/}%name.hrl
%{?_with_debug:install -D -m 0644 {,%buildroot%_otplibdir/%name-%version/}ebin.debug/%name.beam}
%{?_with_native:install -D -m 0644 {,%buildroot%_otplibdir/%name-%version/}ebin.native/%name.beam}


%files -n erlang-%name
%dir %_otplibdir/%name-%version
%_otplibdir/%name-%version/ebin


%if_with debug
%files -n erlang-%name-debug
%dir %_otplibdir/%name-%version
%_otplibdir/%name-%version/ebin.debug
%endif


%if_with native
%files -n erlang-%name-native
%dir %_otplibdir/%name-%version
%_otplibdir/%name-%version/ebin.native
%endif


%files -n erlang-%name-devel
%dir %_otplibdir/%name-%version
%_otplibdir/%name-%version/include


%changelog
* Sun Dec 28 2008 Led <led@altlinux.ru> 0.0-alt0.3
- SVN revision 8
- added subpackages debug, native, devel

* Wed Nov 05 2008 Led <led@altlinux.ru> 0.0-alt0.2
- SVN revision 5

* Mon Aug 18 2008 Led <led@altlinux.ru> 0.0-alt0.1
- initial build
