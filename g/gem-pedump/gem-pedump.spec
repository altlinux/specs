%define        gemname pedump

Name:          gem-pedump
Version:       0.6.5
Release:       alt1
Summary:       dump windows PE files using ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/zed-0xff/pedump
Vcs:           https://github.com/zed-0xff/pedump.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rainbow) >= 0
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(iostruct) >= 0.0.4
BuildRequires: gem(multipart-post) >= 2.0.0
BuildRequires: gem(zhexdump) >= 0.0.2
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(juwelier) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rainbow) >= 0
Requires:      gem(awesome_print) >= 0
Requires:      gem(iostruct) >= 0.0.4
Requires:      gem(multipart-post) >= 2.0.0
Requires:      gem(zhexdump) >= 0.0.2
Obsoletes:     ruby-pedump
Provides:      ruby-pedump
Provides:      gem(pedump) = 0.6.5


%description
A pure ruby implementation of win32 PE binary files dumper.

Supported formats:

* DOS MZ EXE
* win16 NE
* win32 PE
* win64 PE

Can dump:

* MZ/NE/PE Header
* DOS stub
* 'Rich' Header
* Data Directory
* Sections
* Resources
* Strings
* Imports & Exports
* VS_VERSIONINFO parsing
* PE Packer/Compiler detection

a convenient way to upload your PE's to http://pedump.me for a nice HTML tables
with image previews, candies & stuff.


%package       -n pedump
Version:       0.6.5
Release:       alt1
Summary:       dump windows PE files using ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pedump
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pedump) = 0.6.5

%description   -n pedump
dump windows PE files using ruby executable(s).

A pure ruby implementation of win32 PE binary files dumper.

Supported formats:

* DOS MZ EXE
* win16 NE
* win32 PE
* win64 PE

Can dump:

* MZ/NE/PE Header
* DOS stub
* 'Rich' Header
* Data Directory
* Sections
* Resources
* Strings
* Imports & Exports
* VS_VERSIONINFO parsing
* PE Packer/Compiler detection

a convenient way to upload your PE's to http://pedump.me for a nice HTML tables
with image previews, candies & stuff.

%description   -n pedump -l ru_RU.UTF-8
Исполнямка для самоцвета pedump.


%package       -n gem-pedump-doc
Version:       0.6.5
Release:       alt1
Summary:       dump windows PE files using ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pedump
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pedump) = 0.6.5

%description   -n gem-pedump-doc
dump windows PE files using ruby documentation files.

A pure ruby implementation of win32 PE binary files dumper.

Supported formats:

* DOS MZ EXE
* win16 NE
* win32 PE
* win64 PE

Can dump:

* MZ/NE/PE Header
* DOS stub
* 'Rich' Header
* Data Directory
* Sections
* Resources
* Strings
* Imports & Exports
* VS_VERSIONINFO parsing
* PE Packer/Compiler detection

a convenient way to upload your PE's to http://pedump.me for a nice HTML tables
with image previews, candies & stuff.

%description   -n gem-pedump-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pedump.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n pedump
%doc README.md
%_bindir/pedump

%files         -n gem-pedump-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.6.5-alt1
- ^ 0.5.4 -> 0.6.5 (no devel)

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1
- updated (^) 0.5.2 -> 0.5.4
- fixed (!) spec

* Tue Sep 17 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt2
- used (^) Ruby Policy 2.0
- added (+) package with pedump executable
- fixed (!) gem dependency

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Sep 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus
