%define _unpackaged_files_terminate_build 1

Name: colorized-logs
Version: 2.6
Release: alt1
Summary: Tools for logs with ANSI color
License: MIT
Group: File tools
URL: https://github.com/kilobyte/colorized-logs
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
Here's a handful of tools for dealing with logs with ANSI color.

Some tools like gcc, dmesg, grep --color, colordiff, ccze, etc can enhance
their output with color, making reading a lot more pleasant.  The difference
can be as big as between slogging through twenty pages of a build log to
find a failure, and a swift drag of the scroller to do the same within a
second.

Such colored logs can be usually viewed on a terminal or with "less -R";
this package gives you:
 * ansi2html: convert logs to HTML
 * ansi2txt: drop ANSI control codes
 * ttyrec2ansi: drop timing data from ttyrec files
 * pipetty: makes a program think its stdout and stderr are connected to a
   terminal; use as a prefix: "pipetty dmesg|tee"

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/ansi2html
%_man1dir/ansi2html.1.xz
%_bindir/ansi2txt
%_man1dir/ansi2txt.1.xz
%_bindir/ttyrec2ansi
%_man1dir/ttyrec2ansi.1.xz
%_bindir/pipetty
%_man1dir/pipetty.1.xz
%_bindir/lesstty
%_man1dir/lesstty.1.xz
%doc LICENSE

%changelog
* Wed Aug 30 2023 Alexander Makeenkov <amakeenk@altlinux.org> 2.6-alt1
- Initial build for ALT.
