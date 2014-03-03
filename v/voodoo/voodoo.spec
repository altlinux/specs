Name: voodoo
Version: 1.1.3
Release: alt2
Summary: A compiler for the Voodoo programming language
License: LGPLv2.1
Group: Development/Other
URL: http://inglorion.net/software/%name
Source: http://inglorion.net/download/%name-%version.tar
Provides: %{name}c = %version-%release
BuildArch: noarch

BuildRequires: rpm-build-ruby nasm

%description
The Voodoo compiler is a compiler for the Voodoo programming language.
Voodoo is a programming language designed to be a thin abstraction layer over
CPUs' native instruction sets and operating systems' calling conventions.
Operations provided by Voodoo closely correspond to those of common CPU
instruction sets, allowing programs to be expressed with a minimum of overhead.
At the same time, Voodoo is not tied to a specific instruction set, and support
for new CPUs and operating systems can easily be added.


%prep
%setup -q

sed -i -r '1s|^#![[:blank:]]*/usr/bin/env[[:blank:]]+ruby[[:blank:]]*$|#!%__ruby|' \
	bin/%{name}c \
	lib/%name/config.rb.in \
	test/test \
	test/test_language_version.rb \
	test/test_parser.rb \
	test/test_validator.rb \
	%name.gemspec.in


%build
./configure \
	--prefix %_prefix \
	--default-architecture auto \
	--default-format elf
%make_build RUBYLIBDIR=%ruby_sitelibdir


%install
%makeinstall_std RUBYLIBDIR=%ruby_sitelibdir
rm -f %buildroot%_docdir/%name/LICENSE
mv %buildroot%_docdir/%name{,-%version}


%check
%make_build test


%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*
%ruby_sitelibdir/*


%changelog
* Mon Mar 03 2014 Led <led@altlinux.ru> 1.1.3-alt2
- spec: added %%check section

* Mon Mar 03 2014 Led <led@altlinux.ru> 1.1.3-alt1
- initial build
