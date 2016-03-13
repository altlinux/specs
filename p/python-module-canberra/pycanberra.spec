Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
# END SourceDeps(oneline)
%define oldname pycanberra
%global commit 88c53cd44a626ede3b07dab0b548f8bcfda42867
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          python-module-canberra
Summary:       A very basic (and incomplete) wrapper for libcanberra
URL:           https://github.com/psykoyiko/pycanberra/
License:       LGPLv2

# There's no versioning upstream, it's all about the Git hash
Version:       0
Release:       alt2_0.9.git%{shortcommit}.1.1

# There aren't any release yet, I'm downloading straight from the last commit
Source0:       https://github.com/psykoyiko/pycanberra/archive/%{commit}/%{oldname}-%{version}-%{shortcommit}.tar.gz

BuildArch:     noarch

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base
BuildRequires: rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python3-devel

# This will break at run time when libcanberra bumps its soname :(
Requires:      libcanberra
Source44: import.info

%description
A very basic (and incomplete) wrapper of libcanberra for Python 2.


%package -n python3-module-canberra
Group: Other
Summary:       A very basic (and incomplete) wrapper for libcanberra

%description -n python3-module-canberra
A very basic (and incomplete) wrapper of libcanberra for Python 3.


%prep
%setup -q -n pycanberra-%{commit}


%build
# Nothing to build


%install
install -d %{buildroot}%{python_sitelibdir_noarch}
install -p -m 0644 pycanberra.py %{buildroot}%{python_sitelibdir_noarch}

install -d %{buildroot}%{python3_sitelibdir_noarch}
install -p -m 0644 pycanberra.py %{buildroot}%{python3_sitelibdir_noarch}


%files
%doc COPYING README
%{python_sitelibdir_noarch}/pycanberra.py*

%files -n python3-module-canberra
%doc COPYING README
%{python3_sitelibdir_noarch}/pycanberra.py
%{python3_sitelibdir_noarch}/__pycache__/*


%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0-alt2_0.9.git88c53cd.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0-alt2_0.9.git88c53cd.1
- NMU: Use buildreq for BR.

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.9.git88c53cd
- update to new release by fcimport

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.8.git88c53cd
- moved to Sisyphus (closes: #31525)

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.8.git88c53cd
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.6.git65c3b3f
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.4.git65c3b3f
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.3.git65c3b3f
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.git65c3b3f
- initial fc import

