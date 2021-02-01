Name:       dlcall
Version:    0.0
Release:    alt1
License:    GPLv3+
Summary:    Lets you call C library functions from the command line
Group:      System/Base
Source:     %name-%version.tar

%description
The first argument is either a function name or the dynamic
library to load the function from. All subsequent arguments
describe the arguments and function prototype.
Arguments that parse as ints are assumed to be ints, as doubles assumed
to be doubles, and otherwise treated as strings.

%prep
%setup

%build
make

%install
install -D %name %buildroot/%_bindir/%name
install -D %name.1 %buildroot/%_man1dir/%name.1

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Mon Feb 01 2021 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial build for ALT

