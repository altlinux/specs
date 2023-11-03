Name:    hxtools
Version: 20231101
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

* fd0ssh - pipe for password-over-stdin support to ssh
* ofl - Open file lister (replaces fuser and lsof -m)

%package -n ofl
Summary: Open file lister (replaces fuser and lsof -m)
Group: Monitoring
License: WTFPL

%description -n ofl
Lists all processes that have directories or files open or in use within path.
Additionally it can send a signal to these processes to free up a mountpoint
for example.

%package -n fd0ssh
Summary: pipe for password-over-stdin support to ssh
Group: Other
License: LGPL-2.1 or LGPL-3.0

%description -n fd0ssh
This is a wrapper for ssh which reads the password from stdin and sets things
up so that ssh will recall the wrapper to get the password, which will be read
from the parent process using a pipe.

%prep
%setup

%build
%autoreconf
%configure
%make_build -C sadmin ofl fd0ssh

%install
# ofl
install -Dpm0755 sadmin/ofl %buildroot%_bindir/ofl
install -Dpm0644 doc/ofl.1 %buildroot%_man1dir/ofl.1
# fd0ssh
install -Dpm0755 sadmin/fd0ssh %buildroot%_bindir/fd0ssh
install -Dpm0644 doc/fd0ssh.1 %buildroot%_man1dir/fd0ssh.1

%files -n ofl
%_bindir/ofl
%_man1dir/ofl.1*

%files -n fd0ssh
%_bindir/fd0ssh
%_man1dir/fd0ssh.1*

%changelog
* Fri Nov 03 2023 Andrey Cherepanov <cas@altlinux.org> 20231101-alt1
- New version.

* Thu May 04 2023 Andrey Cherepanov <cas@altlinux.org> 20230411-alt1
- New version.

* Wed Sep 29 2021 Andrey Cherepanov <cas@altlinux.org> 20210928-alt1
- New version.

* Mon Aug 30 2021 Andrey Cherepanov <cas@altlinux.org> 20210803-alt2
- Package fd0ssh.
- Fix licenses.

* Mon Aug 30 2021 Andrey Cherepanov <cas@altlinux.org> 20210803-alt1
- Initial build in Sisyphus.
