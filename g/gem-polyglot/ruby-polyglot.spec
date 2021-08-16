%define        gemname polyglot

Name:          gem-polyglot
Version:       0.3.5
Release:       alt2
Summary:       Augment 'require' to load non-ruby file types
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cjheath/polyglot
Vcs:           https://github.com/cjheath/polyglot.git
Packager:      Andrey Cherepanov <cas@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names fixtures
Obsoletes:     ruby-polyglot < %EVR
Provides:      ruby-polyglot = %EVR
Provides:      gem(polyglot) = 0.3.5


%description
The Polyglot library allows a Ruby module to register a loader for the file type
associated with a filename extension, and it augments 'require' to find and load
matching files.

This supports the creation of DSLs having a syntax that is most appropriate to
their purpose, instead of abusing the Ruby syntax.


%package       -n gem-polyglot-doc
Version:       0.3.5
Release:       alt2
Summary:       Augment 'require' to load non-ruby file types documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета polyglot
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(polyglot) = 0.3.5

%description   -n gem-polyglot-doc
Augment 'require' to load non-ruby file types documentation files.

The Polyglot library allows a Ruby module to register a loader for the file type
associated with a filename extension, and it augments 'require' to find and load
matching files.

This supports the creation of DSLs having a syntax that is most appropriate to
their purpose, instead of abusing the Ruby syntax.

%description   -n gem-polyglot-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета polyglot.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-polyglot-doc
%doc README.txt
%ruby_gemdocdir


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.5-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.5-alt1
- New version

* Thu Apr 24 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.4-alt1
- Initial build for ALT Linux
