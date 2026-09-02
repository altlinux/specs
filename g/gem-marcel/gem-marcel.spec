%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname marcel

Name:          gem-marcel
Version:       2.1.0
Release:       alt1
Summary:       Find the mime type of files, examining file, filename and declared type
License:       MIT or Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/basecamp/marcel
Vcs:           https://github.com/basecamp/marcel.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(irb) >= 0
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(nokogiri) >= 1.18.9
BuildRequires: gem(rack) >= 2
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency nokogiri >= 1.18.9,nokogiri < 2
Requires:      ruby >= 3.3
Requires:      gem(irb) >= 0
Requires:      gem(nokogiri) >= 1.18.9
Obsoletes:     ruby-marcel < %EVR
Provides:      ruby-marcel = %EVR
Provides:      marcel = %EVR
Provides:      gem(marcel) = 2.1.0

%description
Marcel attempts to choose the most appropriate content type for a given file by
looking at the binary data, the filename, and any declared type (perhaps passed
as a request header).


%if_enabled    doc
%package       -n gem-marcel-doc
Version:       2.1.0
Release:       alt1
Summary:       Find the mime type of files, examining file, filename and declared type documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета marcel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(marcel) = 2.1.0

%description   -n gem-marcel-doc
Find the mime type of files, examining file, filename and declared type
documentation files.

Marcel attempts to choose the most appropriate content type for a given file by
looking at the binary data, the filename, and any declared type (perhaps passed
as a request header).

%description   -n gem-marcel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета marcel.
%endif


%if_enabled    devel
%package       -n gem-marcel-devel
Version:       2.1.0
Release:       alt1
Summary:       Find the mime type of files, examining file, filename and declared type development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета marcel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(marcel) = 2.1.0
Requires:      gem(bundler) >= 1.7
Requires:      gem(minitest) >= 6.0
Requires:      gem(rack) >= 2
Requires:      gem(rake) >= 13.0
Conflicts:     gem(minitest) >= 7

%description   -n gem-marcel-devel
Find the mime type of files, examining file, filename and declared type
development package.

Marcel attempts to choose the most appropriate content type for a given file by
looking at the binary data, the filename, and any declared type (perhaps passed
as a request header).

%description   -n gem-marcel-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета marcel.
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
%doc APACHE-LICENSE MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-marcel-doc
%doc APACHE-LICENSE MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-marcel-devel
%doc APACHE-LICENSE MIT-LICENSE README.md
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.0.1 -> 2.1.0

* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- > Ruby Policy 2.0
- ^ 0.3.3 -> 1.0.1

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
