Name:           task
Version:        2.1.2
Release:        alt1
Summary:        A command-line todo list manager

Group:          Office
License:        GPLv2+
URL:            http://taskwarrior.org
Source0:        %name-%version.tar
Packager:	Kirill Maslinsky <kirill@altlinux.org>
Patch0:		%name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires:  gcc-c++ libncurses-devel cmake libuuid-devel perl-devel

%description
Task is a command-line todo list manager. It has
support for GTD functionality and includes the
following features: tags, colorful tabular output,
reports and graphs, lots of manipulation commands,
low-level API, abbreviations for all commands and
options, multiuser file locking, recurring tasks.

%prep
%setup -q
%patch0 -p1

%build
%cmake_insource

%install
%makeinstall_std
%find_lang %name
mkdir -p %buildroot%_sysconfdir/bash_completion.d
install -m 644 -T scripts/bash/task.sh %buildroot%_sysconfdir/bash_completion.d/task

%check
make test

%files
%doc %_docdir/%name/*
%_bindir/task
%_man1dir/*
%_man5dir/*
%_sysconfdir/bash_completion.d/%name

%changelog
* Wed Sep 19 2012 Kirill Maslinsky <kirill@altlinux.org> 2.1.2-alt1
- resurrect from orphaned
- version up

* Thu Dec 03 2009 Maxim Ivanov <redbaron at altlinux.org> 1.8.4-alt1
- Version bump

* Tue Sep 15 2009 Maxim Ivanov <redbaron at altlinux.org> 1.8.2-alt1
- Initial build for ALT Linux. Fedora spec adapted.

