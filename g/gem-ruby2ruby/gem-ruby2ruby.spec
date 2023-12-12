%define        _unpackaged_files_terminate_build 1
%define        gemname ruby2ruby

Name:          gem-ruby2ruby
Version:       2.5.0
Release:       alt1
Summary:       ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/ruby2ruby
Vcs:           https://github.com/seattlerb/ruby2ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(sexp_processor) >= 4.6
BuildRequires: gem(ruby_parser) >= 3.1
BuildRequires: gem(hoe) >= 0
BuildConflicts: gem(sexp_processor) >= 5
BuildConflicts: gem(ruby_parser) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(sexp_processor) >= 4.6
Requires:      gem(ruby_parser) >= 3.1
Conflicts:     gem(sexp_processor) >= 5
Conflicts:     gem(ruby_parser) >= 4
Obsoletes:     ruby2ruby < %EVR
Provides:      ruby2ruby = %EVR
Provides:      gem(ruby2ruby) = 2.5.0

%ruby_bindir_to %ruby_bindir

%description
ruby2ruby provides a means of generating pure ruby code easily from RubyParser
compatible Sexps. This makes making dynamic language processors in ruby easier
than ever!


%package       -n r2r-show
Version:       2.5.0
Release:       alt1
Summary:       ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby2ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby2ruby) = 2.5.0

%description   -n r2r-show
ruby2ruby provides a means of generating pure ruby code easily from RubyParser
compatible Sexps executable(s).

ruby2ruby provides a means of generating pure ruby code easily from RubyParser
compatible Sexps. This makes making dynamic language processors in ruby easier
than ever!

%description   -n r2r-show -l ru_RU.UTF-8
Исполнямка для самоцвета ruby2ruby.


%package       -n gem-ruby2ruby-doc
Version:       2.5.0
Release:       alt1
Summary:       ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby2ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby2ruby) = 2.5.0

%description   -n gem-ruby2ruby-doc
ruby2ruby provides a means of generating pure ruby code easily from RubyParser
compatible Sexps documentation files.

ruby2ruby provides a means of generating pure ruby code easily from RubyParser
compatible Sexps. This makes making dynamic language processors in ruby easier
than ever!

%description   -n gem-ruby2ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby2ruby.


%package       -n gem-ruby2ruby-devel
Version:       2.5.0
Release:       alt1
Summary:       ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby2ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby2ruby) = 2.5.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 0

%description   -n gem-ruby2ruby-devel
ruby2ruby provides a means of generating pure ruby code easily from RubyParser
compatible Sexps development package.

ruby2ruby provides a means of generating pure ruby code easily from RubyParser
compatible Sexps. This makes making dynamic language processors in ruby easier
than ever!

%description   -n gem-ruby2ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby2ruby.


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

%files         -n r2r-show
%doc README.rdoc
%ruby_bindir/r2r_show

%files         -n gem-ruby2ruby-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-ruby2ruby-devel
%doc README.rdoc


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.4.4 -> 2.5.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.4-alt1
- updated (^) 2.4.3 -> 2.4.4
- fixed (-) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.3-alt1.1
- fixed (!) spec according to changelog rules

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.3-alt1
- updated (^) 2.4.2 -> 2.4.3
- added (+) rpm "r2r_show" build
- fixed (!) spec

* Sat Mar 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt2
- Use Ruby Policy 2.0
- Bump to 2.4.2

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
