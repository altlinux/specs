Summary: Tool to generate password/passwords hash
Name: makepasswd
Version: 0.5.1
Release: alt1
Url: http://people.defora.org/~khorben/projects/makepasswd/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: System/Base


%description
Makepasswd generates (pseudo-)random passwords of a desired length.
It is able to generate its crypted equivalent.

%prep
%setup

%build
%make

%install
install -D -m 755 src/makepasswd %buildroot%_sbindir/makepasswd
install -D -m 644 makepasswd.1.gz %buildroot%_man1dir/makepasswd.1.gz

%files
%_sbindir/makepasswd
%_man1dir/makepasswd.1.gz
%changelog
* Tue Feb 19 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.1-alt1
- Initial build

