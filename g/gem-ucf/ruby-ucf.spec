%define        gemname ucf

Name:          gem-ucf
Version:       2.0.2
Release:       alt1
Summary:       This is a Ruby library for working with UCF documents
License:       BSD
Group:         Development/Ruby
Url:           http://mygrid.github.io/ruby-ucf/
Vcs:           https://github.com/mygrid/ruby-ucf.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rdoc) >= 4.1 gem(rdoc) < 7.0
BuildRequires: gem(test-unit) >= 3.0 gem(test-unit) < 4
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(nokogiri) >= 1.6 gem(nokogiri) < 2
BuildRequires: gem(zip-container) >= 4.0.1 gem(zip-container) < 4.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 10.0,rake < 14.0
%ruby_use_gem_dependency rdoc >= 4.1,rdoc < 7.0
Requires:      gem(zip-container) >= 4.0.1 gem(zip-container) < 4.1
Obsoletes:     ruby-ucf < %EVR
Provides:      ruby-ucf = %EVR
Provides:      gem(ucf) = 2.0.2

%description
This is a Ruby library for working with UCF documents. See the specification at
https://learn.adobe.com/wiki/display/PDFNAV/Universal+Container+Format for more
details. UCF is a type of EPUB and very similar to the EPUB Open Container
Format (OCF).


%package       -n gem-ucf-doc
Version:       2.0.2
Release:       alt1
Summary:       Universal Container Format (UCF) Ruby Library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ucf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ucf) = 2.0.2

%description   -n gem-ucf-doc
Universal Container Format (UCF) Ruby Library documentation files.

A Ruby library for working with Universal Container Format files - a type of
EPUB document. See the UCF specification
(https://learn.adobe.com/wiki/display/PDFNAV/Universal+Container+Format) for
details. They are very similar, although not as restrictive, as the EPUB Open
Container Format (OCF) (http://www.idpf.org/epub/30/spec/epub30-ocf.html).

%description   -n gem-ucf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ucf.


%package       -n gem-ucf-devel
Version:       2.0.2
Release:       alt1
Summary:       Universal Container Format (UCF) Ruby Library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ucf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ucf) = 2.0.2
Requires:      gem(rake) >= 10.0 gem(rake) < 14.0
Requires:      gem(bundler) >= 0
Requires:      gem(rdoc) >= 4.1 gem(rdoc) < 7.0
Requires:      gem(test-unit) >= 3.0 gem(test-unit) < 4
Requires:      gem(coveralls) >= 0
Requires:      gem(nokogiri) >= 1.6 gem(nokogiri) < 2

%description   -n gem-ucf-devel
Universal Container Format (UCF) Ruby Library development package.

A Ruby library for working with Universal Container Format files - a type of
EPUB document. See the UCF specification
(https://learn.adobe.com/wiki/display/PDFNAV/Universal+Container+Format) for
details. They are very similar, although not as restrictive, as the EPUB Open
Container Format (OCF) (http://www.idpf.org/epub/30/spec/epub30-ocf.html).

%description   -n gem-ucf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ucf.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc ReadMe.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ucf-doc
%doc ReadMe.rdoc
%ruby_gemdocdir

%files         -n gem-ucf-devel
%doc ReadMe.rdoc


%changelog
* Thu Apr 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt1
- ^ 2.0.0 -> 2.0.2

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux (without tests)
