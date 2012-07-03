Name: verborum-caterva
Version: 2.0
Release: alt2

Source:%name-%version.tar.gz

Packager: Paul Wolneykien <manowar@altlinux.ru>

Summary: Simple engine for arbitrary file structure generation
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: rpm-macros-alterator rpm-macros-fillup

%description
Verborum Caterva is a simple engine for arbitrary file structure
generation. File hierarchy to be built is represented as another file
hierarchy called a "template structure" or just as "template" for
short.

Each file to be built is represented in a template as a directory with
a number of files and no subdirectories. The files a called "portions"
are processed in alphabetical order for target file to be built.

Each portion is either a plain file in wich case its contents are
simply appended to the target file, or it may be an executable
program. In a latter case the program is executed and its output is
appended to the target file.

A directory in a template which contains only other directories is not
a file template howewer. Directories of that kind are just recreated
in a target hierarchy. Program behavior on a mixed case template
directory (i.e., containing files and directories) is undefined.

CAUTION! This program might create a much huge lot of useless files
for you if it would be run in wrong place on FS! It doesn't recognize
with directory is a template and which is not and would process
everything!

%prep
%setup -q

%install
install -p -m0755 -D verborum-caterva %buildroot%_bindir/verborum-caterva
install -p -m0755 -D verborum-caterva-valtable %buildroot%_bindir/verborum-caterva-valtable

%files
%_bindir/verborum-caterva
%_bindir/verborum-caterva-valtable

%changelog
* Tue Jun 02 2009 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt2
- Value table API.

* Thu May 28 2009 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt1
- Use transitional script istead of direct data generation (by raorn@).

* Wed Apr 15 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Do not delete or move destination directories by default.

* Tue Apr 14 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Backup system.

* Sun Apr 12 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Value table.

* Wed Apr 08 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release.
