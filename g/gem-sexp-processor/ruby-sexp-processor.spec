%define        gemname sexp_processor

Name:          gem-sexp-processor
Version:       4.16.0
Release:       alt1
Summary:       sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/sexp_processor
Vcs:           https://github.com/seattlerb/sexp_processor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names sexp_processor,sexp-processor
Obsoletes:     ruby-sexp_processor < %EVR
Provides:      ruby-sexp_processor = %EVR
Provides:      gem(sexp_processor) = 4.16.0


%description
sexp_processor branches from ParseTree bringing all the generic sexp processing
tools with it. Sexp, SexpProcessor, Environment, etc... all for your language
processing pleasure.


%package       -n gem-sexp-processor-doc
Version:       4.16.0
Release:       alt1
Summary:       sexp_processor branches from ParseTree bringing all the generic sexp processing tools with it documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sexp_processor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sexp_processor) = 4.16.0

%description   -n gem-sexp-processor-doc
sexp_processor branches from ParseTree bringing all the generic sexp processing
tools with it documentation files.

sexp_processor branches from ParseTree bringing all the generic sexp processing
tools with it. Sexp, SexpProcessor, Environment, etc... all for your language
processing pleasure.

%description   -n gem-sexp-processor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sexp_processor.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-sexp-processor-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Fri Apr 01 2022 Pavel Skrylev <majioa@altlinux.org> 4.16.0-alt1
- ^ 4.15.0 -> 4.16.0

* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 4.15.0-alt1
- ^ 4.12.1 -> 4.15.0
- * renamed

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 4.12.1-alt1
- ^ 4.11.0 -> 4.12.1
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1
- Initial build for Sisyphus
