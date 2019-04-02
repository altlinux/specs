%define _unpackaged_files_terminate_build 1

Name: gmonitor
Version: 1.2
Release: alt2

# 15 Aug 2018

Summary: This is a GPU monitoring program.

License: GPLv3
Group: Development/Other
Url: https://github.com/mountassir/gmonitor

Source: %name-%version.tar
Source1: README_ALT.md
Patch0: gmonitor-alt-cmakelists.patch

BuildRequires: gcc-c++ cmake rpm-macros-cmake nvidia-settings

%description
This is a GPU monitoring program, it monitors the core usage, VRAM usage, 
PCI-E & memory bus usage and the temperature of the GPU. 
I write CUDA programs and always needed a way to monitor how they behave in real time, 
searched for an MSI afterburner like programs on GNU/Linux systems but couldn't find any, 
so I decided to put this together and have been using it for quite some time now.
Though this is quite minimal, it's good enough for what I needed it.

%prep
%setup
%patch0 -p1
cp -f %SOURCE1 .

%build
%cmake_insource
%make_build

%install
%makeinstall_std gmonitordir=%_bindir/gmonitor

%files
%doc README.md COPYING README_ALT.md
%_bindir/%name

%changelog
* Tue Apr 02 2019 Pavel Moseev <mars@altlinux.org> 1.2-alt2
- added README_ALT.md

* Tue Aug 15 2018 Pavel Moseev <mars@altlinux.org> 1.2-alt1
- initial build
