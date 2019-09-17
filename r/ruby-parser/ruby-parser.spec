%define        pkgname ruby-parser
%define        gemname ruby_parser

Name:          %pkgname
Version:       3.13.1
Release:       alt1
Summary:       ruby_parser (RP) is a ruby parser written in pure ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/ruby_parser
%vcs           https://github.com/seattlerb/ruby_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: unifdef
BuildRequires: gem(hoe)
BuildRequires: gem(sexp_processor)
BuildRequires: gem(oedipus_lex)
BuildRequires: gem(racc)

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc-which does by default use a C extension). RP's output is the same
as ParseTree's output: s-expressions using ruby's arrays and base types.


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
%ruby_build ́--pre=repackage --use=%gemname --alias=parser --join=bin:lib --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%_bindir/*

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt1
- ^ v3.13.1
- ! spec

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ v3.13.0
- + using setup gem's dependency detection

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.12.0-alt1
- ^ v3.12.0
- ^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- Initial build for Sisyphus
