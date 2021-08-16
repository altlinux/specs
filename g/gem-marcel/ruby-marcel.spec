%define        gemname marcel

Name:          gem-marcel
Version:       1.0.1
Release:       alt1
Summary:       Find the mime type of files, examining file, filename and declared type
License:       MIT or Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/basecamp/marcel
Vcs:           https://github.com/basecamp/marcel.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-rack-test
BuildRequires: ruby-mimemagic
BuildRequires: gem(minitest) >= 5.11 gem(minitest) < 6
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-marcel < %EVR
Provides:      ruby-marcel = %EVR
Provides:      gem(marcel) = 1.0.1


%description
Marcel attempts to choose the most appropriate content type for a given file by
looking at the binary data, the filename, and any declared type (perhaps passed
as a request header).


%package       -n gem-marcel-doc
Version:       1.0.1
Release:       alt1
Summary:       Find the mime type of files, examining file, filename and declared type documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета marcel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(marcel) = 1.0.1

%description   -n gem-marcel-doc
Find the mime type of files, examining file, filename and declared type
documentation files.

Marcel attempts to choose the most appropriate content type for a given file by
looking at the binary data, the filename, and any declared type (perhaps passed
as a request header).

%description   -n gem-marcel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета marcel.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-marcel-doc
%ruby_gemdocdir


%changelog
* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- > Ruby Policy 2.0
- ^ 0.3.3 -> 1.0.1

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
