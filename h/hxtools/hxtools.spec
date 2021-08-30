Name:    hxtools
Version: 20210803
Release: alt1

Summary: A collection of several tools
License: GPLv2+ or LGPLv2 or LGPLv3
Group: Other
URL: http://inai.de/projects/hxtools/
# VCS: https://git.inai.de/hxtools

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libHX-devel

%description
hxtools contains several tools for different tasks written by Jan Engelhardt.

Currently only these tools are included in package:

* ofl - Open file lister (replaces fuser and lsof -m)

%package -n ofl
Summary: Open file lister (replaces fuser and lsof -m)
Group: Monitoring

%description -n ofl
Lists all processes that have directories or files open or in use within path.
Additionally it can send a signal to these processes to free up a mountpoint
for example.

%prep
%setup

%build
%autoreconf
%configure
%make_build -C sadmin ofl
%make_build -C doc ofl.1

%install
# ofl
install -Dpm0755 sadmin/ofl %buildroot%_bindir/ofl
install -Dpm0644 doc/ofl.1 %buildroot%_man1dir/ofl.1

%files -n ofl
%_bindir/ofl
%_man1dir/ofl.1*

%changelog
* Mon Aug 30 2021 Andrey Cherepanov <cas@altlinux.org> 20210803-alt1
- Initial build in Sisyphus.
