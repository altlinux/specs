Name: python3-module-slob
Version: 1.0
Release: alt0.git.x.g81fbdc.1
Summary: Aard SLOB module
BuildArch: noarch
Group: Development/Python
Url: http://aarddict.org
License: GPL3

#https://github.com/itkach/slob.git
Source: slob.tar

BuildPreReq: rpm-build-python3

%description
Read-only compressed data store

%prep
%setup -n slob

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir --record=INSTALLED_FILES

%files
%python3_sitelibdir/[Ss]lob*
%doc LICENSE README*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt0.git.x.g81fbdc.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Dec 07 2014 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt0.git.x.g81fbdc
- initial build for ALT Linux Sisyphus
