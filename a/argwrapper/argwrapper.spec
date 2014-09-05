# TODO generate version
Name:		argwrapper
Version:	0.02
Release:	alt1
Source:		%name-%version.tar
License:	GPLv3
Group:		File tools
Summary:	Run a binary with environment and arguments sewed into wrapper name

BuildRequires:	txt2man glibc-devel-static

%description

When called without parameters, argwrapper assumes it's a wrapper call.
It parses it's zero argument (argv[0], usually binary file name) and
splits it into series of environment variables assignments, wrapped
program name and command line arguments.

When called with some command line parameters, argwrapper assumes it's
a filename generator call. It selects a character for argument
separator, a replacement characters for '/' path separator and other
optional chars, if any. It's guaranteed that none of the characters
selected is appeared within original command line. Then '/' and optional
chars are replaced with corresponded replacements and all the arguments
are concatenated with argument separator.

%prep
%setup

%build
%make release

%install
install -D %name %buildroot%_bindir/%name
install -D %name.1 %buildroot%_man1dir/%name.1

%check
make check

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Fri Sep 05 2014 Fr. Br. George <george@altlinux.ru> 0.02-alt1
- Initial build

