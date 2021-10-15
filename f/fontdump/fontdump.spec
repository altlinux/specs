Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%{?python_enable_dependency_generator}
%global srcname fontdump
%global sum Dump the CSS and different formats of fonts for Google Fonts

Name:           %{srcname}
Version:        1.3.0
Release:        alt2_25
Summary:        %{sum}

License:        MIT
URL:            https://github.com/glasslion/fontdump
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-module-fontdump
Source44: import.info

%description
A command line tool to dump the CSS and different formats of fonts for Google
Fonts, so you can serve them on your local servers.

%package -n python3-module-fontdump
Group: Publishing
Summary:        %{sum}
BuildRequires:   python3-module-distribute
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
%python3_build

%install
%python3_install

%check
%{__python3} setup.py test

%files
%{_bindir}/%{srcname}

%files -n python3-module-fontdump
%doc PKG-INFO
%doc --no-dereference LICENSE
%{python3_sitelibdir_noarch}/%{srcname}
%{python3_sitelibdir_noarch}/%{srcname}-%{version}-py3.*.egg-info

%changelog
* Fri Oct 15 2021 Igor Vlasenko <viy@altlinux.org> 1.3.0-alt2_25
- update to new release by fcimport

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_19
- update

* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- python2 disabled

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_11
- update to new release by fcimport

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1_9.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_9
- update to new release by fcimport

* Fri Nov 06 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2
- new version

