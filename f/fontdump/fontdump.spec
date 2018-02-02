Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: python3-module-setuptools
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname fontdump
%global sum Dump the CSS and different formats of fonts for Google Fonts

Name:           %{srcname}
Version:        1.3.0
Release:        alt1_9.1
Summary:        %{sum}

License:        MIT
URL:            https://github.com/glasslion/fontdump
Source0:        http://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel python3-devel
Requires:       python3-module-fontdump
Requires:       python3-module-cssutils
Requires:       python3-module-docopt
Requires:       python3-module-requests
Source44: import.info

%description
A command line tool to dump the CSS and different formats of fonts for Google
Fonts, so you can serve them on your local servers.

%package -n python-module-fontdump
Group: Publishing
Summary:        %{sum}
BuildRequires:   python-module-docopt
BuildRequires:   python-module-cssutils
BuildRequires:   python-module-requests
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python-module-fontdump
A command line tool to dump the CSS and different formats of fonts for Google
Fonts, so you can serve them on your local servers.


%package -n python3-module-fontdump
Group: Publishing
Summary:        %{sum}
BuildRequires:   python3-module-docopt
BuildRequires:   python3-module-cssutils
BuildRequires:   python3-module-requests
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-module-fontdump
A command line tool to dump the CSS and different formats of fonts for Google
Fonts, so you can serve them on your local servers.

%prep
%setup -q -n %{srcname}-%{version}

sed -i -e '/^#!\//, 1d' fontdump/*.py

%build
%python_build
%python3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%python_install
%python3_install

%check
%{__python} setup.py test
%{__python3} setup.py test

%files
%{_bindir}/%{srcname}

%files -n python-module-fontdump
%doc PKG-INFO
%doc LICENSE
%{python_sitelibdir_noarch}/%{srcname}
%{python_sitelibdir_noarch}/%{srcname}-%{version}-py2.*.egg-info

%files -n python3-module-fontdump
%doc PKG-INFO
%doc LICENSE
%{python3_sitelibdir_noarch}/%{srcname}
%{python3_sitelibdir_noarch}/%{srcname}-%{version}-py3.*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1_9.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_9
- update to new release by fcimport

* Fri Nov 06 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2
- new version

