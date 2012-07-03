Name: ext3grep
Version: 0.10.2
Release: alt1.1

License: GPL
Url: http://code.google.com/p/ext3grep/
Packager: Evgeny V. Shishkov <shev@altlinux.org>

Summary: A tool to investigate an ext3 file system for deleted content and possibly recover it.
Group: File tools
Source: %name-%version.tar.gz
Patch0: %name-alt-e2fsprogs.patch

# Automatically added by buildreq on Wed Jan 21 2009
BuildRequires: gcc-c++ libe2fs-devel

%description
A tool to investigate an ext3 file system for deleted content and possibly recover it.

%description -l ru_RU.UTF-8
Утилита исследования файловой системы ext3 на удалённое содержимое и, возможно, восстановления.

%prep
%setup -q
%patch0 -p2

%build
%configure

%make_build

%install
%make_install DESTDIR="%buildroot/" install

%files
%_bindir/%name
%doc LICENSE.GPL2 NEWS README

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.1
- Fixed build

* Fri Apr 23 2010 Evgeny V. Shishkov <shev@altlinux.org> 0.10.2-alt1
- new version
    Added support for --restore-inode=<ino>@<journal-sequence-number>

* Wed Jan 21 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.10.1-alt1
- initial build.
