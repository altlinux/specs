%define oname maintboot

Name: python3-module-%oname
Version: 0.1.0
Release: alt1

Summary: maintboot runs commands outside of the current OS
License: GPLv3
Group: Development/Python3
Url: https://github.com/g2p/maintboot
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-devel


%description
maintboot runs commands outside of the current OS, with exclusive access to the system and hardware.

This can be useful to run maintenance tasks, like repartitioning, in a controlled environment.

Maintboot builds an appliance on the fly from a list of packages (using supermin). It then loads the appliance with kexec, bypassing the bios, and runs the maintenance script in that new context.

%prep
%setup

%build
%python3_build

%install
%python3_install

install -d %buildroot%_sbindir
mv %buildroot{%_bindir,%_sbindir}/%oname

%files
%doc README.md
%_sbindir/%oname
%python3_sitelibdir/*


%changelog
* Mon May 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux Sisyphus
