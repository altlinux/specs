%define _unpackaged_files_terminate_build 1

Name: quickemu
Version: 4.9.9
Release: alt1

Summary: Quickly create and run optimised Windows, macOS and Linux virtual machines
License: MIT
Group: Emulators
Url: https://github.com/quickemu-project/quickemu

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Requires: edk2-tools
Requires: qemu
Requires: qemu-ui-sdl
Requires: libspice-gtk-tools
Requires: swtpm
Requires: xrandr

%description
Quickemu is a wrapper for the excellent QEMU that automatically
"does the right thing" when creating virtual machines.
No requirement for exhaustive configuration options. You decide what
operating system you want to run and Quickemu takes care of the rest.

* quickget automatically downloads the upstream OS and creates
  the configuration;
* quickemu enumerates your hardware and launches the virtual machine
  with the optimum configuration best suited to your computer.

The original objective of the project was to enable quick testing of
Linux distributions where the virtual machines and their configuration
can be stored anywhere (such as external USB storage or your home
directory) and no elevated permissions are required to run the virtual
machines.

Today, Quickemu includes comprehensive support for macOS, Windows, most
of the BSDs, novel non-Linux operating systems such as FreeDOS, Haiku,
KolibriOS, OpenIndiana, ReactOS, and more.

%prep
%setup

%install
# binaries
install -Dpm755 chunkcheck %buildroot%_bindir/chunkcheck
install -Dpm755 quickemu %buildroot%_bindir/quickemu
install -Dpm755 quickget %buildroot%_bindir/quickget
install -Dpm755 quickreport %buildroot%_bindir/quickreport

# docs
install -Dpm644 docs/quickemu_conf.5 %buildroot%_man5dir/quickemu_conf.5
install -Dpm644 docs/quickemu.1 %buildroot%_man1dir/quickemu.1
install -Dpm644 docs/quickget.1 %buildroot%_man1dir/quickget.1

%files
%doc LICENSE *.md
%_bindir/chunkcheck
%_bindir/quickemu
%_bindir/quickget
%_bindir/quickreport
%_man5dir/quickemu_conf.5*
%_man1dir/quickemu.1*
%_man1dir/quickget.1*

%changelog
* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 4.9.9-alt1
- Initial build for Sisyphus
