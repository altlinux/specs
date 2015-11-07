Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define fedora 22
%if 0%{?fedora} >= 23 || 0%{?rhel} >= 8
%global ftpackage python2-fonttools
%else
%global ftpackage fonttools
%endif

Name:           ttname
Version:        1
Release:        alt1_6
Summary:        CLI font metadata editor
BuildArch:      noarch

License:        BSD
URL:            https://github.com/tchollingsworth/ttname
Source0:        https://pypi.python.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
# upstream commit 0a352b9a3b6aeb558e3cd4d2939a24321dd7b0dc
Patch0:         0001-fix-output-with-unicode-characters.patch
# https://github.com/tchollingsworth/ttname/pull/1
Patch1:         0002-cope-with-fonttools-2.5.patch
Patch2:         0003-deal-better-with-stdout-as-output.patch

BuildRequires:  python-devel python-module-setuptools

# for tests
BuildRequires:  python-module-fonttools
BuildRequires:  python-module-nose
BuildRequires:  python-module-lxml
BuildRequires:  fontconfig

# for entrypoint magic
Requires:       python-module-setuptools
# for normal runtime
Requires:       python-module-fonttools
Requires:       python-module-lxml
Source44: import.info

%description
A CLI interface for editing the "name" table that contains the metadata in
TrueType and OpenType fonts.

%prep
%setup -q

%patch0 -p1 -b .unicode
%patch1 -p1 -b .fonttools25
%patch2 -p1 -b .stdout

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
nosetests -vx
 
%files
%{python_sitelibdir_noarch}/ttname
%{python_sitelibdir_noarch}/ttname-*.egg-info
%{_bindir}/ttname
%{_mandir}/man1/ttname.1.*
%doc LICENSE

%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1-alt1_6
- new version

