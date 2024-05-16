%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname image_processing

Name:          gem-image-processing
Version:       1.12.2
Release:       alt1
Summary:       High-level wrapper for processing images for the web with ImageMagick or libvips
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janko/image_processing
Vcs:           https://github.com/janko/image_processing.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 5.8
BuildRequires: gem(minitest-hooks) >= 1.4.2
BuildRequires: gem(minispec-metadata) >= 0
BuildRequires: gem(dhash-vips) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(mini_magick) >= 4.9.5
BuildRequires: gem(ruby-vips) >= 2.0.17
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mini_magick) >= 5
BuildConflicts: gem(ruby-vips) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(mini_magick) >= 4.9.5
Requires:      gem(ruby-vips) >= 2.0.17
Conflicts:     gem(mini_magick) >= 5
Conflicts:     gem(ruby-vips) >= 3
Provides:      gem(image_processing) = 1.12.2


%description
High-level wrapper for processing images for the web with ImageMagick or
libvips.


%if_enabled    doc
%package       -n gem-image-processing-doc
Version:       1.12.2
Release:       alt1
Summary:       High-level wrapper for processing images for the web with ImageMagick or libvips documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета image_processing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(image_processing) = 1.12.2

%description   -n gem-image-processing-doc
High-level wrapper for processing images for the web with ImageMagick or libvips
documentation files.

%description   -n gem-image-processing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета image_processing.
%endif


%if_enabled    devel
%package       -n gem-image-processing-devel
Version:       1.12.2
Release:       alt1
Summary:       High-level wrapper for processing images for the web with ImageMagick or libvips development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета image_processing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(image_processing) = 1.12.2
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 5.8
Requires:      gem(minitest-hooks) >= 1.4.2
Requires:      gem(minispec-metadata) >= 0
Requires:      gem(dhash-vips) >= 0
Requires:      gem(pry) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-image-processing-devel
High-level wrapper for processing images for the web with ImageMagick or libvips
development package.

%description   -n gem-image-processing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета image_processing.
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
%files         -n gem-image-processing-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-image-processing-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.12.2-alt1
- + packaged gem with Ruby Policy 2.0
