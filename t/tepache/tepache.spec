Group: Development/Python
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           tepache
Version:        1.1.2
Release:        alt1_14
Summary:        Code sketcher for python

License:        LGPLv2+
URL:            http://launchpad.net/tepache
Source0:        http://launchpad.net/tepache/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:         tepache-1.1.2-rev_6.patch

BuildArch:      noarch
BuildRequires:  python-devel
Source44: import.info

%description
Tepache is a code sketcher for python that uses pygtk and glade. It could look
like other glade codegens, but it is totally different. Not a glade
codegen but a code sketcher.


%prep
%setup -q
%patch0 -p0


%build
%python_build


%install
%python_install

# Python scripts in site-packages should not be executible
#sed -i -e 's,#!/usr/bin/env python,#,g' %{buildroot}%{python_sitelibdir_noarch}/*.py

 
%files
%doc README
%{_bindir}/tepache
%{python_sitelibdir_noarch}/*


%changelog
* Fri Jul 12 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_14
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.1-alt1.1
- Rebuilt with python-2.5.

* Fri Aug 26 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1-alt1
- Initial build for Sisyphus.


