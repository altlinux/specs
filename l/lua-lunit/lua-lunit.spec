%define luaver 5.2
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-lunit
Version:        0.5
Release:        alt1_10
Summary:        Unit testing framework for Lua

Group:          Development/Other
License:        MIT
URL:            http://nessie.de/mroth/lunit/index.html
Source0:        http://nessie.de/mroth/lunit/lunit-%{version}.tar.gz

# for running tests
BuildRequires:  lua >= %{luaver}
Requires:       lua >= %{luaver}

BuildArch:      noarch
Source44: import.info

%description
Lunit is a unit testing framework for lua, written in lua.

Lunit provides 26 assert functions, and a few misc functions for usage
in an easy unit testing framework.

Lunit comes with a test suite to test itself. The testsuite consists
of approximately 710 assertions.


%prep
%setup -q -n lunit-%{version}


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p lunit $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
cp -pr lunit{,-console}.lua $RPM_BUILD_ROOT%{luapkgdir}


%check
./lunit lunit-tests.lua | tee testlog.txt
grep -q "0 failed, 0 errors" testlog.txt


%files
%doc LICENSE ANNOUNCE CHANGES DOCUMENTATION README* example.lua
%{_bindir}/lunit
%{luapkgdir}/*


%changelog
* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5-alt1_10
- converted for ALT Linux by srpmconvert tools

