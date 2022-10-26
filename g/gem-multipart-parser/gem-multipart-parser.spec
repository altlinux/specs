%define        gemname multipart-parser

Name:          gem-multipart-parser
Version:       0.1.1.1
Release:       alt1
Summary:       simple parser for multipart MIME messages
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/danabr/multipart-parser
Vcs:           https://github.com/danabr/multipart-parser.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(multipart-parser) = 0.1.1.1

%ruby_use_gem_version multipart-parser:0.1.1.1

%description
multipart-parser is a simple parser for multipart MIME messages, written in
Ruby, based on felixge/node-formidable's parser.

Some things to note:
- Pure Ruby
- Event-driven API
- Only supports one level of multipart parsing. Invoke another parser if you
need to handle nested messages.
- Does not perform I/O.
- Does not depend on any other library.


%package       -n gem-multipart-parser-doc
Version:       0.1.1.1
Release:       alt1
Summary:       simple parser for multipart MIME messages documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета multipart-parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(multipart-parser) = 0.1.1.1

%description   -n gem-multipart-parser-doc
simple parser for multipart MIME messages documentation files.

multipart-parser is a simple parser for multipart MIME messages, written in
Ruby, based on felixge/node-formidable's parser.

Some things to note:
- Pure Ruby
- Event-driven API
- Only supports one level of multipart parsing. Invoke another parser if you
need to handle nested messages.
- Does not perform I/O.
- Does not depend on any other library.

%description   -n gem-multipart-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета multipart-parser.


%package       -n gem-multipart-parser-devel
Version:       0.1.1.1
Release:       alt1
Summary:       simple parser for multipart MIME messages development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета multipart-parser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(multipart-parser) = 0.1.1.1

%description   -n gem-multipart-parser-devel
simple parser for multipart MIME messages development package.

multipart-parser is a simple parser for multipart MIME messages, written in
Ruby, based on felixge/node-formidable's parser.

Some things to note:
- Pure Ruby
- Event-driven API
- Only supports one level of multipart parsing. Invoke another parser if you
need to handle nested messages.
- Does not perform I/O.
- Does not depend on any other library.

%description   -n gem-multipart-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета multipart-parser.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-multipart-parser-doc
%doc README
%ruby_gemdocdir

%files         -n gem-multipart-parser-devel
%doc README


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
