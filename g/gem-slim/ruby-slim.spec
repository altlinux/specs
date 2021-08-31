%define        gemname slim

Name:          gem-slim
Version:       4.1.0
Release:       alt1
Summary:       Slim is a template language whose goal is to reduce the syntax to the essential parts without becoming cryptic
License:       MIT
Group:         Development/Ruby
Url:           http://slim-lang.com/
Vcs:           https://github.com/slim-template/slim.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(temple) >= 0.7.6 gem(temple) < 0.9
BuildRequires: gem(tilt) >= 2.0.6 gem(tilt) < 2.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(temple) >= 0.7.6 gem(temple) < 0.9
Requires:      gem(tilt) >= 2.0.6 gem(tilt) < 2.1
Obsoletes:     ruby-slim < %EVR
Provides:      ruby-slim = %EVR
Provides:      gem(slim) = 4.1.0


%description
Slim is a template language whose goal is to reduce the view syntax to the
essential parts without becoming cryptic. It started as an exercise to see how
much could be removed from a standard html template (<, >, closing tags, etc...)
As more people took an interest in Slim, the functionality grew and so did the
flexibility of the syntax.


%package       -n slimrb
Version:       4.1.0
Release:       alt1
Summary:       Slim is a template language whose goal is to reduce the syntax to the essential parts without becoming cryptic executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета slim
Group:         Other
BuildArch:     noarch

Requires:      gem(slim) = 4.1.0

%description   -n slimrb
Slim is a template language whose goal is to reduce the syntax to the essential
parts without becoming cryptic executable(s).

Slim is a template language whose goal is to reduce the view syntax to the
essential parts without becoming cryptic. It started as an exercise to see how
much could be removed from a standard html template (<, >, closing tags, etc...)
As more people took an interest in Slim, the functionality grew and so did the
flexibility of the syntax.

%description   -n slimrb -l ru_RU.UTF-8
Исполнямка для самоцвета slim.


%package       -n gem-slim-doc
Version:       4.1.0
Release:       alt1
Summary:       Slim is a template language whose goal is to reduce the syntax to the essential parts without becoming cryptic documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета slim
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(slim) = 4.1.0

%description   -n gem-slim-doc
Slim is a template language whose goal is to reduce the syntax to the essential
parts without becoming cryptic documentation files.

Slim is a template language whose goal is to reduce the view syntax to the
essential parts without becoming cryptic. It started as an exercise to see how
much could be removed from a standard html template (<, >, closing tags, etc...)
As more people took an interest in Slim, the functionality grew and so did the
flexibility of the syntax.

%description   -n gem-slim-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета slim.


%package       -n gem-slim-devel
Version:       4.1.0
Release:       alt1
Summary:       Slim is a template language whose goal is to reduce the syntax to the essential parts without becoming cryptic development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета slim
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(slim) = 4.1.0

%description   -n gem-slim-devel
Slim is a template language whose goal is to reduce the syntax to the essential
parts without becoming cryptic development package.

Slim is a template language whose goal is to reduce the view syntax to the
essential parts without becoming cryptic. It started as an exercise to see how
much could be removed from a standard html template (<, >, closing tags, etc...)
As more people took an interest in Slim, the functionality grew and so did the
flexibility of the syntax.

%description   -n gem-slim-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета slim.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.jp.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n slimrb
%doc README.jp.md README.md
%_bindir/slimrb

%files         -n gem-slim-doc
%doc README.jp.md README.md
%ruby_gemdocdir

%files         -n gem-slim-devel
%doc README.jp.md README.md


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 4.1.0-alt1
- ^ 3.0.9 -> 4.1.0

* Sun Feb 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.9-alt1
- Initial build for Sisyphus
