Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
# END SourceDeps(oneline)
%define oldname libssh2-python
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global __provides_exclude_from ^(%{python_sitelibdir}/.*\\.so)$
%global __provides_exclude_from ^(%{python3_sitelibdir}/.*\\.so)$

Summary:        Python binding for the libssh2 library
Name:           python-module-libssh2
Version:        0.7.1
Release:        alt1_18.1
License:        LGPLv2+
URL:            https://github.com/wallunit/ssh4py
# The source for the package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone git://github.com/wallunit/ssh4py.git
#  cd ssh4py ; python setup.py sdist
Source0:        https://github.com/wallunit/ssh4py/zipball/0.7.1/%{oldname}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:  libssh2-devel
BuildRequires:  libssl-devel
BuildRequires:  zlib-devel

%global _description\
libssh2-python is a python binding for the libssh2 library\

Source44: import.info


%description %_description

%package -n python3-module-libssh2
Group: Development/Other
Summary:        %summary
%{?python_provide:%python_provide python3-libssh2}
# Remove before F30
Provides:       libssh2-python = %{version}-%{release}
Provides:       libssh2-python = %{version}-%{release}
Obsoletes:      libssh2-python < %{version}-%{release}

%description -n python3-module-libssh2 %_description


%prep
%setup -n %{oldname}-%{version} -q


%build
%python_build
%python3_build


%install
%python_install
%python3_install
mv %{buildroot}%{python3_sitelibdir}/libssh2.*.so %{buildroot}%{python3_sitelibdir}/libssh2.so


%files -n python-module-libssh2
%doc README.txt COPYING
%{python_sitelibdir}/libssh2.so
%{python_sitelibdir}/libssh2*-*.egg-info

%files -n python3-module-libssh2
%doc README.txt COPYING
%{python3_sitelibdir}/libssh2.so
%{python3_sitelibdir}/libssh2*-*.egg-info


%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1_18.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Oct 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_13
- update to new release by fcimport

* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_11
- converted for ALT Linux by srpmconvert tools

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.1-alt1_3.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_3
- initial import by fcimport

