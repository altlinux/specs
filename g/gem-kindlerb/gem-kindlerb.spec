%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname kindlerb

Name:          gem-kindlerb
Version:       1.2.1
Release:       alt0.2
Summary:       Kindle periodical format ebook generation tool
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/danchoi/kindlerb
Vcs:           https://github.com/danchoi/kindlerb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(mustache) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(nokogiri) >= 0
Requires:      gem(mustache) >= 0
Obsoletes:     ruby-kindlerb < %EVR
Provides:      ruby-kindlerb = %EVR
Provides:      gem(kindlerb) = 1.2.1


%description
kindlerb is a Ruby Kindle periodical-format ebook generator. This tool was
initially extracted from kindlefeeder.com. Kindlefodder was also built on top of
kindlerb. kindlerb converts a file tree of sections, articles, images, and
metadata into a MOBI periodical-formatted document for the Kindle. It is a
wrapper around the kindlegen program from Amazon that hides the details for
templating OPF and NCX files.


%package       -n setupkindlerb
Version:       1.2.1
Release:       alt0.2
Summary:       Kindle periodical format ebook generation tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета kindlerb
Group:         Other
BuildArch:     noarch

Requires:      gem(kindlerb) = 1.2.1

%description   -n setupkindlerb
Kindle periodical format ebook generation tool executable(s).

kindlerb is a Ruby Kindle periodical-format ebook generator. This tool was
initially extracted from kindlefeeder.com. Kindlefodder was also built on top of
kindlerb. kindlerb converts a file tree of sections, articles, images, and
metadata into a MOBI periodical-formatted document for the Kindle. It is a
wrapper around the kindlegen program from Amazon that hides the details for
templating OPF and NCX files.

%description   -n setupkindlerb -l ru_RU.UTF-8
Исполнямка для самоцвета kindlerb.


%if_enabled    doc
%package       -n gem-kindlerb-doc
Version:       1.2.1
Release:       alt0.2
Summary:       Kindle periodical format ebook generation tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kindlerb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kindlerb) = 1.2.1

%description   -n gem-kindlerb-doc
Kindle periodical format ebook generation tool documentation files.

kindlerb is a Ruby Kindle periodical-format ebook generator. This tool was
initially extracted from kindlefeeder.com. Kindlefodder was also built on top of
kindlerb. kindlerb converts a file tree of sections, articles, images, and
metadata into a MOBI periodical-formatted document for the Kindle. It is a
wrapper around the kindlegen program from Amazon that hides the details for
templating OPF and NCX files.

%description   -n gem-kindlerb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kindlerb.
%endif


%if_enabled    devel
%package       -n gem-kindlerb-devel
Version:       1.2.1
Release:       alt0.2
Summary:       Kindle periodical format ebook generation tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kindlerb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kindlerb) = 1.2.1

%description   -n gem-kindlerb-devel
Kindle periodical format ebook generation tool development package.

kindlerb is a Ruby Kindle periodical-format ebook generator. This tool was
initially extracted from kindlefeeder.com. Kindlefodder was also built on top of
kindlerb. kindlerb converts a file tree of sections, articles, images, and
metadata into a MOBI periodical-formatted document for the Kindle. It is a
wrapper around the kindlegen program from Amazon that hides the details for
templating OPF and NCX files.

%description   -n gem-kindlerb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kindlerb.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n setupkindlerb
%doc README.md
%_bindir/setupkindlerb

%if_enabled    doc
%files         -n gem-kindlerb-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-kindlerb-devel
%doc README.md
%endif


%changelog
* Fri May 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt0.2
- * rename to proper name

* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt0.1
- ^ 1.2.0 -> 1.2.1pre

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
