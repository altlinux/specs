%define gitdate git20131106

Name: skippy-xd
Version: 0.5
Release: alt1.%gitdate

Summary: Full-screen task-switcher for X11
License: %gpl2plus
Group: Graphical desktop/Other

URL: http://code.google.com/p/skippy-xd/
# git://github.com/richardgv/skippy-xd.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-build-xdg

BuildRequires: libX11-devel libXcomposite-devel libXdamage-devel libXext-devel
BuildRequires: libXfixes-devel libXft-devel libXinerama-devel libXrender-devel
BuildRequires: libpng-devel zlib-devel libjpeg-devel libgif-devel

%description
Standalone composited window picker (displays all your windows at once,
with live previews).

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags"
%make_build PREFIX=%_prefix SKIPPYXD_VERSION=%version-%gitdate

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc CHANGELOG README.asciidoc
%_xdgconfigdir/*.rc
%_bindir/*


%changelog
* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20131106
- Upstream git snapshot.

* Wed Jun 19 2013 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20130602
- Initial build.

