%define oname slob

Name: python3-module-slob
Version: 1.0.2
Release: alt1.git.x.g018588
Summary: Aard SLOB module
Group: Development/Python3
Url: http://aarddict.org
License: GPL3
BuildArch: noarch

#https://github.com/itkach/slob.git
Source: slob.tar
Source44: %name.watch

# Automatically added by buildreq on Wed Jan 26 2022
# optimized out: python3 python3-base python3-dev python3-module-pkg_resources sh4
BuildRequires: python3-module-setuptools

%description
Read-only compressed data store

%prep
%setup -n slob

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir --record=INSTALLED_FILES

%files
%_bindir/*
%python3_sitelibdir/[Ss]lob*
%doc LICENSE README*

%changelog
* Wed Jan 26 2022 Ildar Mulyukov <ildar@altlinux.ru> 1.0.2-alt1.git.x.g018588
- new version

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt0.git.x.g81fbdc.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt0.git.x.g81fbdc.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Dec 07 2014 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt0.git.x.g81fbdc
- initial build for ALT Linux Sisyphus
