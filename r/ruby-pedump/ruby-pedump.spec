%define        pkgname pedump

Name: 	       ruby-%pkgname
Version:       0.5.2
Release:       alt2
Summary:       dump windows PE files using ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/zed-0xff/pedump
%vcs           http://github.com/zed-0xff/pedump.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%gem_replace_version multipart-post ~> 2.0
%add_findreq_skiplist %ruby_gemslibdir/**/*

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


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 17 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt2
- ^ Ruby Policy 2.0
- ! gem dependency
- + package with pedump executable

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Sep 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus
