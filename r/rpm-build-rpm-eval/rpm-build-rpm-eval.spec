Name: rpm-build-rpm-eval
Version: 0.1
Release: alt3

Summary: The script disclosure macros in files
Summary(ru_RU.KOI8-R): Скрипт раскрывающий макросы в файлах
License: %gpl2plus
Group: Development/Other
Packager: Aleksey Avdeev <solo@altlinux.ru>

%define rpmeval_name rpm-eval.sh
%define rpmeval_dir %_datadir/%name
%define rpmeval %rpmeval_dir/%rpmeval_name

Source1: rpm-eval.sh
# rpm macro definitions
Source2: rpm-eval-rpm-macros.spec.inc

# include rpm-eval-rpm-macros.spec.inc
%include %SOURCE2

BuildPreReq: rpm-build-licenses

Provides: %rpmeval

BuildArch: noarch

%description
The package contains a script disclosure rpm macros in files.

%description -l ru_RU.KOI8-R
Пакет содержит скрипт раскрывающий rpm макросы в файлах.
   

%package -n rpm-macros-rpm-eval
Summary: RPM macros for use rpm-eval.sh
Summary(ru_RU.KOI8-R): RPM макросы для применения rpm-eval.sh
Group: Development/Other

%description -n rpm-macros-rpm-eval
These macros provide for use rpm-eval.sh to build packages.

%description -n rpm-macros-rpm-eval -l ru_RU.KOI8-R
Макросы для  применения rpm-eval.sh при сборке пакетов.
в соответствии с Alt Linux Team Policy.


%prep
%setup -cTn %name-%version

%build
sed -e 's/^%%define[[:space:]]\+/%%/' %SOURCE2 > rpm-eval.rpm-macros

%install
install -D -m755 %SOURCE1 %buildroot%rpmeval

install -pD -m644 rpm-eval.rpm-macros \
	%buildroot%_sysconfdir/rpm/macros.d/%name

%files
%dir %rpmeval_dir/
%rpmeval

%files -n rpm-macros-rpm-eval
%_sysconfdir/rpm/macros.d/%name

%changelog
* Fri Aug 29 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt3
- Add build subpackage for ALT Linux Team Policy compatible way:
  + rpm-macros-rpm-eval

* Wed Aug 27 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt2
- Add %%_datadir/%%name/rpm-eval.sh provides

* Wed Aug 27 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build
