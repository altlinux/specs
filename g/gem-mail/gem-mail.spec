%define        gemname mail

Name:          gem-mail
Version:       2.8.1
Release:       alt1
Summary:       A really Ruby Mail handler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mikel/mail
Vcs:           https://github.com/mikel/mail.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.0.3
BuildRequires: gem(rake) > 0.8.7
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-benchmark) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rufo) >= 0
BuildRequires: gem(mini_mime) >= 0.1.1
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(strscan) >= 3.0.2
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(net-imap) >= 0
BuildRequires: gem(net-pop) >= 0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(mini_mime) >= 0.1.1
Requires:      gem(net-smtp) >= 0
Requires:      gem(net-imap) >= 0
Requires:      gem(net-pop) >= 0
Obsoletes:     ruby-mail < %EVR
Provides:      ruby-mail = %EVR
Provides:      gem(mail) = 2.8.1


%description
Mail is an internet library for Ruby that is designed to handle emails
generation, parsing and sending in a simple, rubyesque manner.


%package       -n gem-mail-doc
Version:       2.8.1
Release:       alt1
Summary:       A really Ruby Mail handler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mail) = 2.8.1

%description   -n gem-mail-doc
A really Ruby Mail handler documentation files.

Mail is an internet library for Ruby that is designed to handle emails
generation, parsing and sending in a simple, rubyesque manner.

%description   -n gem-mail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mail.


%package       -n gem-mail-devel
Version:       2.8.1
Release:       alt1
Summary:       A really Ruby Mail handler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mail) = 2.8.1
Requires:      gem(bundler) >= 1.0.3
Requires:      gem(rake) > 0.8.7
Requires:      gem(rspec) >= 3.0
Requires:      gem(rdoc) >= 0
Requires:      gem(rufo) >= 0
Requires:      gem(byebug) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-mail-devel
A really Ruby Mail handler development package.

Mail is an internet library for Ruby that is designed to handle emails
generation, parsing and sending in a simple, rubyesque manner.

%description   -n gem-mail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mail.


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

%files         -n gem-mail-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mail-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 2.8.1-alt1
- ^ 2.7.1[1] -> 2.8.1

* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.1.1-alt0.1
- ^ 2.7.1 -> 2.7.1[1]
- * renamed

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.1-alt2
- > Ruby Policy 2.0

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Nov 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version

* Sat Jun 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- New version

* Thu Apr 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version
- Disable test because they require network connections

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 2.5.4-alt1
- Initial build for ALT Linux
