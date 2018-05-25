%define oname aar2slob

%def_with bootstrap

Name: python3-module-%oname
Version: 0.01
Release: alt2.1

Summary: converts Aard Dictionary .aar files to slob format
Group: Development/Other
License: GPL3
Url: http://aarddict.org
#https://github.com/itkach/aar2slob.git
BuildArch: noarch

Source: %name.tar

%if_with bootstrap
%py3_requires cssselect
%endif

BuildRequires(pre): rpm-build-python3


%description
converts Aard Dictionary .aar files to slob format

%prep
%setup -n %name

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir --record=INSTALLED_FILES

%files
%python3_sitelibdir/%{oname}*
%doc README*

%changelog
* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.01-alt2.1
- rebuild with all requires

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.01-alt2
- rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.01-alt1.git.x.gf1956a.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Feb 14 2015 Ildar Mulyukov <ildar@altlinux.ru> 0.01-alt1.git.x.gf1956a
- initial build for ALT Linux Sisyphus
