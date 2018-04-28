Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define fedora 26
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} >= 23 || 0%{?rhel} >= 8
%global ftpackage python2-fonttools
%else
%global ftpackage fonttools
%endif

Name:           ttname
Version:        1
Release:        alt2_11
Summary:        CLI font metadata editor
BuildArch:      noarch

License:        BSD
URL:            https://github.com/tchollingsworth/ttname
Source0:        https://files.pythonhosted.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
# upstream commit 0a352b9a3b6aeb558e3cd4d2939a24321dd7b0dc
Patch0:         0001-fix-output-with-unicode-characters.patch
Patch1:         0002-cope-with-fonttools-3.1.0.patch
Patch2:         0003-deal-better-with-stdout-as-output.patch

Patch10:        ttname-alt-build.patch

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

%patch10 -p2

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
* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1-alt2_11
- Fixed build.

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1_11
- update to new release by fcimport

* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 1-alt1_6
- new version

