Name: screencaster
Version: 0.1
Release: alt1

Summary: Screencaster
Packager: Dmitry Derjavin <dd@altlinux.org> 
License: GPL
Group: Video
Url: http://git.altlinux.org/people/dd/packages/screencaster.git

Source: %name-%version.tar

BuildArch: noarch

Requires: ffmpeg

%description
ffmpeg based screencaster

%prep
%setup

%install
mkdir -p -m755 %buildroot%_bindir
cp -a recstart %buildroot%_bindir
cp -a recstop %buildroot%_bindir

%files
%doc screencasterrc
%_bindir/*

%changelog
* Sun Jan 30 2011 Dmitry Derjavin <dd@altlinux.org> 0.1-alt1
- Initial release. Spec file by sin@altlinux.org.
