# Generated File.
%setup_docs_module tomcat_conf ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: Installation and setup of Tomcat 5.5 on ALT Linux Master 2.4
Summary(ru_RU.KOI8-R): Установка и конфигурирование Tomcat 5.5 на ALT Linux Master 2.4
License: %fdl
Url: http://www.geodigital.ru/pub/docs/tomcat/tomcat5_setup_howto.html
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-tomcat_conf-jlev
Provides: docs-tomcat_conf-jlev
Obsoletes: docs-tomcat_conf-jlev

Source: %name-%version.tar

%description
Following Tomcat configuration issues are covered: Tomcat 5.5 installation; server launching in daemon mode on 80 port; virtual hosts setup; write mode for access logs; Webalizer; logrotate setup.

%description -l ru_RU.KOI8-R
Описаны следующие вопросы конфигурирования Tomcat: Установка tomcat 5.5; Запуск сервера в качестве демона на 80 порту; Настройка виртуальных хостов; Включение режима записи access логов; Подключение Webalizer; Настройка logrotate.

%prep
%setup

%build
%docs_module_build "html" "tomcat5_setup_howto.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-tomcat_conf-jlev -> docs-tomcat_conf
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050516-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050516-alt1
- Auto build with new version.

