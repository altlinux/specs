%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-vips

Name:          gem-ruby-vips
Version:       2.2.1
Release:       alt1
Summary:       A fast image processing library with low memory needs
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/libvips/ruby-vips
Vcs:           https://github.com/libvips/ruby-vips.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rspec) >= 3.3
BuildRequires: gem(yard) >= 0.9.11
BuildRequires: gem(bundler) >= 1.0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(ffi) >= 1.12
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(ffi) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(ffi) >= 1.12
Conflicts:     gem(ffi) >= 2
Provides:      gem(ruby-vips) = 2.2.1


%description
ruby-vips is a binding for the libvips image processing library. It is fast and
it can process large images without loading the whole image in memory.


%if_enabled    doc
%package       -n gem-ruby-vips-doc
Version:       2.2.1
Release:       alt1
Summary:       A fast image processing library with low memory needs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-vips
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-vips) = 2.2.1

%description   -n gem-ruby-vips-doc
A fast image processing library with low memory needs documentation
files.

ruby-vips is a binding for the libvips image processing library. It is fast and
it can process large images without loading the whole image in memory.

%description   -n gem-ruby-vips-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-vips.
%endif


%if_enabled    devel
%package       -n gem-ruby-vips-devel
Version:       2.2.1
Release:       alt1
Summary:       A fast image processing library with low memory needs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-vips
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-vips) = 2.2.1
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.3
Requires:      gem(yard) >= 0.9.11
Requires:      gem(bundler) >= 1.0
Requires:      gem(standard) >= 0
Requires:      gem(github-markup) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1
Conflicts:     gem(bundler) >= 3

%description   -n gem-ruby-vips-devel
A fast image processing library with low memory needs development
package.

ruby-vips is a binding for the libvips image processing library. It is fast and
it can process large images without loading the whole image in memory.

%description   -n gem-ruby-vips-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-vips.
%endif


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

%if_enabled    doc
%files         -n gem-ruby-vips-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-vips-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- + packaged gem with Ruby Policy 2.0
