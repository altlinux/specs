Name: fhs
Version: 2.3
Release: alt1

Summary: Filesystem Hierarchy Standard
License: distributable
Group: Development/Other
Url: http://www.pathname.com/fhs
BuildArch: noarch

Source0: %url/pub/%name-%version.ps.bz2
Source1: %url/pub/%name-%version.txt.bz2
Source2: %name-%version.ChangeLog

%description
This standard consists of a set of requirements and guidelines
for file and directory placement under UNIX-like operating systems.
The guidelines are intended to support interoperability of applications,
system administration tools, development tools, and scripts as well as
greater uniformity of documentation for these systems.

%prep
%setup -qcT
%__install -pm644 %_sourcedir/%name-%version.ps.bz2 %name.ps.bz2
%__install -pm644 %_sourcedir/%name-%version.txt.bz2 %name.txt.bz2
%__install -pm644 %_sourcedir/%name-%version.ChangeLog ChangeLog

%files
%doc *

%changelog
* Sat Sep 03 2005 Dmitry V. Levin <ldv@altlinux.org> 2.3-alt1
- Updated to FHS-2.3.

* Sun Oct 20 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt3
- Don't build pdf docs.
- Fixed to built witn new groff.
- Updated buildrequires.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt2
- Added buildrequires.

* Tue Aug 13 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt1
- Initial revision.
