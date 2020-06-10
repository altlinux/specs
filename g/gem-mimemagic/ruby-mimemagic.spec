%define        pkgname mimemagic

Name:          gem-%pkgname
Version:       0.3.5
Release:       alt1
Summary:       Mime type detection in ruby via file extension or file content
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/minad/mimemagic
#Vcs:           https://github.com/minad/mimemagic.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

MimeMagic is a library to detect the mime type of a file by extension or by
content. It uses the mime database provided by freedesktop.org


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

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.5-alt1
- ^ 0.3.2 -> 0.3.5
- ! spec name and syntax

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
