%global realname parsedatetime

%define py3dir %_builddir/%name-%version-py3dir
%def_with python3

Name: python-module-parsedatetime
Version: 1.5
Release: alt1.1

Summary: Parse human-readable date/time strings in Python

Group: Development/Python
License: ASL 2.0
Url: https://github.com/bear/%realname

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://github.com/bear/%realname/archive/v%version.tar.gz#/%realname-%version.tar.gz
Patch: fix-non-executable-script-init.patch

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-epydoc

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

%description
parsedatetime is a python module that can parse human-readable date/time
strings.

%package doc
Group: Development/Python
Summary: Documentation for the parsedatetime python module

%description doc
This package contains the generated HTML documentation for the
parsedatetime python module

%if_with python3
%package -n python3-module-%realname
Group: Development/Python
Summary: Parse human-readable date/time strings in Python

%description -n python3-module-%realname
parsedatetime is a python module that can parse human-readable date/time
strings.
%endif

%prep
%setup -n %realname-%version
%patch0 -p1

# Fixes spurious-executable-perm warning
chmod 644 implementation_notes.txt

%if_with python3
rm -rf %py3dir
cp -a . %py3dir
%endif

%build
%python_build

# Build documentation
epydoc --html --config epydoc.conf

%if_with python3
pushd %py3dir
%python3_build
popd
%endif

%install
%python_install
# It makes no sense to ship all these tests in the package
# just use them during the build
rm -rf %buildroot%python_sitelibdir/%realname/tests

%if_with python3
pushd %py3dir
%python3_install
# It makes no sense to ship all these tests in the package
# just use them during the build
rm -rf %buildroot%python3_sitelibdir/%realname/tests
popd
%endif

%check
#__python run_tests.py

#if_with python3
#pushd %py3dir
#__python3 run_tests.py test
#endif

%files
%doc LICENSE.txt
%doc AUTHORS.txt CHANGES.txt INSTALL.txt README.rst THANKS.txt
%python_sitelibdir/%realname
%python_sitelibdir/%realname-%version-*.egg-info

%files doc
%doc docs/ examples/ implementation_notes.txt locale_date_grouping_notes.txt

%if_with python3
%files -n python3-module-%realname
%doc LICENSE.txt
%doc AUTHORS.txt CHANGES.txt INSTALL.txt README.rst THANKS.txt
%python3_sitelibdir/%realname/
%python3_sitelibdir/%{realname}*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 17 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 02 2015 Michele Baldessari <michele@acksyn.org> - 1.5-1
- New upstream (BZ#1238670)
* Mon Jun 22 2015 Michele Baldessari <michele@acksyn.org> - 1.4-2
- Fix python --> python2 macros
* Thu Jun 04 2015 Michele Baldessari <michele@acksyn.org> - 1.4-1
- Initial packaging
