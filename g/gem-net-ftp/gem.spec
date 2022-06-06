%define        gemname net-ftp

Name:          gem-net-ftp
Version:       0.1.3
Release:       alt1
Summary:       Support for the File Transfer Protocol
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/net-ftp
Vcs:           https://github.com/ruby/net-ftp.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(net-protocol) >= 0
BuildRequires: gem(time) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(net-protocol) >= 0
Requires:      gem(time) >= 0
Provides:      gem(net-ftp) = 0.1.3


%description
This class implements the File Transfer Protocol. If you have used a
command-line FTP program, and are familiar with the commands, you will be able
to use this class easily. Some extra features are included to take advantage of
Ruby's style and strengths.


%package       -n gem-net-ftp-doc
Version:       0.1.3
Release:       alt1
Summary:       Support for the File Transfer Protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-ftp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-ftp) = 0.1.3

%description   -n gem-net-ftp-doc
Support for the File Transfer Protocol documentation files.

This class implements the File Transfer Protocol. If you have used a
command-line FTP program, and are familiar with the commands, you will be able
to use this class easily. Some extra features are included to take advantage of
Ruby's style and strengths.

%description   -n gem-net-ftp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-ftp.


%package       -n gem-net-ftp-devel
Version:       0.1.3
Release:       alt1
Summary:       Support for the File Transfer Protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-ftp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-ftp) = 0.1.3

%description   -n gem-net-ftp-devel
Support for the File Transfer Protocol development package.

This class implements the File Transfer Protocol. If you have used a
command-line FTP program, and are familiar with the commands, you will be able
to use this class easily. Some extra features are included to take advantage of
Ruby's style and strengths.

%description   -n gem-net-ftp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-ftp.


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

%files         -n gem-net-ftp-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-net-ftp-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.3-alt1
- + packaged gem with Ruby Policy 2.0
