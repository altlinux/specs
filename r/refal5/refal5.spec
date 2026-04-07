%define        _unpackaged_files_terminate_build 1

Name:          refal5
Version:       230918.1
Release:       alt1
Summary:       Refal-5 is a dialect of Refal developed at the City College of New York
License:       Unlicense
Group:         Development/Other
Url:           http://www.botik.ru/pub/local/scp/refal5/
Vcs:           http://refal.botik.ru/refal5/

Source:        %name-%version.tar

%description
Refal (for REcursive Functions Algorithmic Language) is a functional
programming language oriented toward symbol manipulation: string processing,
translation, artificial intelligence. Functional programming languages enjoy
well-deserved popularity nowadays. One of the oldest members of this family
(first implemented in 1968 in Russia, where it has been widely used ever since),
Refal combines mathematical simplicity with practicality for writing big and
sophisticated programs.

Refal-5 is a dialect of Refal developed at the City College of New York. The
features included in Refal-5 have been tested by time.

%prep
%setup

%build
%make_build

%install
install -D -m755 -t %buildroot%_bindir/ crefal refc refgo reftr


%files
%_bindir/*

%changelog
* Tue Apr 07 2026 Pavel Skrylev <majioa@altlinux.org> 230918.1-alt1
- + packaged gem with Ruby Policy 2.0
