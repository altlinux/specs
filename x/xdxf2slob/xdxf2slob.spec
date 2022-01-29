Name: xdxf2slob
Version: 0.0
Release: alt1
Summary: tool to convert XDXF dictionary files to slob format
License: GPL3
Group: Text tools
Url: http://aarddict.org
Source: %name-%version.tar
Source44: %name.watch
BuildArch: noarch

# Automatically added by buildreq on Wed Jan 26 2022 (-bi)
# optimized out: python3 python3-base python3-dev python3-module-pkg_resources rpm-build-python3 rpm-macros-python3 sh4
BuildRequires: python3-module-setuptools

Requires: python3-module-slob >= 1.0.2

%description
XDXF -> slob

%prep
%setup

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir --record=INSTALLED_FILES

%files
%doc README*
%_bindir/*
%python3_sitelibdir/%{name}*

%changelog
* Wed Jan 26 2022 Ildar Mulyukov <ildar@altlinux.ru> 0.0-alt1
- Initial build for Sisyphus
