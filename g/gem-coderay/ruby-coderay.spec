%define        gemname coderay

Name:          gem-coderay
Version:       1.1.3
Release:       alt1
Summary:       Fast and easy syntax highlighting for selected languages, written in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubychan/coderay
Vcs:           https://github.com/rubychan/coderay.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-coderay < %EVR
Provides:      ruby-coderay = %EVR
Provides:      gem(coderay) = 1.1.3

%description
CodeRay is a Ruby library for syntax highlighting.

You put your code in, and you get it back colored; Keywords, strings, floats,
comments - all in different colors. And with line numbers.


%package       -n coderay
Version:       1.1.3
Release:       alt1
Summary:       Fast syntax highlighting for selected languages. executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета coderay
Group:         Other
BuildArch:     noarch

Requires:      gem(coderay) = 1.1.3

%description   -n coderay
Fast syntax highlighting for selected languages. executable(s).

Fast and easy syntax highlighting for selected languages, written in Ruby. Comes
with RedCloth integration and LOC counter.

%description   -n coderay -l ru_RU.UTF-8
Исполнямка для самоцвета coderay.


%package       -n gem-coderay-doc
Version:       1.1.3
Release:       alt1
Summary:       Fast syntax highlighting for selected languages. documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета coderay
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(coderay) = 1.1.3

%description   -n gem-coderay-doc
Fast syntax highlighting for selected languages. documentation files.

Fast and easy syntax highlighting for selected languages, written in Ruby. Comes
with RedCloth integration and LOC counter.

%description   -n gem-coderay-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета coderay.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README_INDEX.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n coderay
%doc README_INDEX.rdoc
%_bindir/coderay

%files         -n gem-coderay-doc
%doc README_INDEX.rdoc
%ruby_gemdocdir


%changelog
* Tue May 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ 1.1.2 -> 1.1.3

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Oct 21 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.1.1-alt1
- Initial build in Sisyphus
