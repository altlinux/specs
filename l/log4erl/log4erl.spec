%def_with debug
%def_with native

Name: log4erl
Version: 0.8.2
Release: alt1
Summary: A logger for Erlang in the spirit of Log4J
URL: http://code.google.com/p/%name/
License: %mpl
Group: Development/Erlang
Source: http://%name.googlecode.com/files/%name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: erlang erlang-otp-devel rpm-build-erlang symlinks

%description
%name is a logger for Erlang in the spirit of Log4J.
Features:
  - Multiple file logs
  - Currently, only size-based log rotation of files
  - Support default logger if no logger specified
  - 5 predefined log levels (debug, info, warn, error, fatal)
  - Support for user-specified log levels


%package -n erlang-%name
Summary: A logger for Erlang in the spirit of Log4J
Group: Development/Erlang
BuildArch: noarch
Provides: %name = %version-%release
Requires: erlang-%name-common = %version-%release

%description -n erlang-%name
%name is a logger for Erlang in the spirit of Log4J.
Features:
  - Multiple file logs
  - Currently, only size-based log rotation of files
  - Support default logger if no logger specified
  - 5 predefined log levels (debug, info, warn, error, fatal)
  - Support for user-specified log levels


%package -n erlang-%name-common
Summary: A logger for Erlang in the spirit of Log4J - common files
Group: Development/Erlang
BuildArch: noarch
Provides: %name-common = %version-%release

%description -n erlang-%name-common
%name is a logger for Erlang in the spirit of Log4J.
Features:
  - Multiple file logs
  - Currently, only size-based log rotation of files
  - Support default logger if no logger specified
  - 5 predefined log levels (debug, info, warn, error, fatal)
  - Support for user-specified log levels
This package contains common files for %name modules.


%if_with debug
%package -n erlang-%name-debug
Summary: A logger for Erlang in the spirit of Log4J - modules with debug information
Group: Development/Erlang
BuildArch: noarch
Provides: %name-debug = %version-%release
Requires: erlang-%name-common = %version-%release

%description -n erlang-%name-debug
%name is a logger for Erlang in the spirit of Log4J.
Features:
  - Multiple file logs
  - Currently, only size-based log rotation of files
  - Support default logger if no logger specified
  - 5 predefined log levels (debug, info, warn, error, fatal)
  - Support for user-specified log levels
This package contains modules with debug information.
%endif


%if_with native
%package -n erlang-%name-native
Summary: A logger for Erlang in the spirit of Log4J - modules with native CPU code
Group: Development/Erlang
Provides: %name-native = %version-%release
Requires: erlang-%name-common = %version-%release

%description -n erlang-%name-native
%name is a logger for Erlang in the spirit of Log4J.
Features:
  - Multiple file logs
  - Currently, only size-based log rotation of files
  - Support default logger if no logger specified
  - 5 predefined log levels (debug, info, warn, error, fatal)
  - Support for user-specified log levels
This package contains modules with native CPU code.
%endif


%prep
%setup
%patch -p1


%build
%make_build ERLC_FLAGS="%{?eoptflags:%eoptflags}"
%if_with debug
mkdir ebin.debug
%make_build -C src ERLC_FLAGS="%{?eoptflags:%eoptflags} +debug_info" EBIN_DIR=../ebin.debug
%endif
%if_with native
mkdir ebin.native
%make_build -C src ERLC_FLAGS="%{?eoptflags:%eoptflags} +native +'{hipe,[o2]}'" EBIN_DIR=../ebin.native
%endif


%install
install -d -m 0755 %buildroot{%_otplibdir/%name-%version/{ebin,include,priv},%_docdir/erlang-%name-%version}
install -m 0644 ebin/* %buildroot%_otplibdir/%name-%version/ebin/
%if_with debug
install -d -m 0755 %buildroot%_otplibdir/%name-%version/ebin.debug
install -m 0644 ebin.debug/* %buildroot%_otplibdir/%name-%version/ebin.debug/
ln -sf ../ebin/%name.app %buildroot%_otplibdir/%name-%version/ebin.debug/
%endif
%if_with native
install -d -m 0755 %buildroot%_otplibdir/%name-%version/ebin.native
install -m 0644 ebin.native/* %buildroot%_otplibdir/%name-%version/ebin.native/
ln -sf ../ebin/%name.app %buildroot%_otplibdir/%name-%version/ebin.native/
%endif
install -m 0644 priv/*.conf %buildroot%_otplibdir/%name-%version/priv/
install -m 0644 include/* %buildroot%_otplibdir/%name-%version/include/
install -m 0644 {CHANGELOG,README,TODO}.txt %buildroot%_otplibdir/%name-%version/
for f in CHANGELOG README TODO; do
    ln -sf %buildroot%_otplibdir/%name-%version/$f.txt %buildroot%_docdir/erlang-%name-%version/$f
done
symlinks -sc %buildroot%_docdir/erlang-%name-%version


%files -n erlang-%name-common
%dir %_otplibdir/%name-%version
%dir %_otplibdir/%name-%version/ebin
%_otplibdir/%name-%version/ebin/*.app
%_otplibdir/%name-%version/include
%_otplibdir/%name-%version/priv
%doc %_otplibdir/%name-%version/*.txt
%doc %_docdir/erlang-%name-%version


%files -n erlang-%name
%_otplibdir/%name-%version/ebin/*.beam


%if_with debug
%files -n erlang-%name-debug
%_otplibdir/%name-%version/ebin.debug
%endif


%if_with native
%files -n erlang-%name-native
%_otplibdir/%name-%version/ebin.native
%endif


%changelog
* Sat Dec 27 2008 Led <led@altlinux.ru> 0.8.2-alt1
- 0.8.2
- add subpackages: common, debug, native
- removed subpackage examples

* Sun Oct 05 2008 Led <led@altlinux.ru> 0.8.1-alt2
- updated BuildRequires

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Mon Jul 28 2008 Led <led@altlinux.ru> 0.7-alt2
- buiit with erlang-R12B

* Tue Jul 01 2008 Led <led@altlinux.ru> 0.7-alt1
- initial build
