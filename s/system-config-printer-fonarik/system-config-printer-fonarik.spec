%define _unpackaged_files_terminate_build 1

Name:           system-config-printer-fonarik
Version:        0.1.0
Release:        alt4
Summary:        "Fonarik" plugin for the GTK printer job viewer
Summary(ru_RU.UTF-8): Добавляет операцию "Маркировка задания" в менеджер печати на GTK
License:        GPLv3+
Group:          System/Configuration/Printing
Url:            http://git.altlinux.org/people/manowar/packages/%{name}.git

Source:         fonarik-%version.tar
BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-cups >= 1.9.74-alt2
BuildRequires: python3-module-pluggy

%description
The plugin adds the "Mark Job" context menu item. By invoking this action
a user can enter the desired job metadata and print it along with the job.

%description -l ru_RU.UTF-8
Этот плагин добавляет операцию "Маркировка задания" по которой пользователь
может ввессти желаемые метаданные, которые будет напечатаны вместе
с документом.

%package -n python3-module-%name
Summary:        "Fonarik" plugin for the GTK printer job viewer
Summary(ru_RU.UTF-8): Добавляет операцию "Маркировка задания" в менеджер печати на GTK
License:        GPLv3+
Group:          System/Configuration/Printing
Requires:       system-config-printer >= 1.5.11-alt12
Requires:       python3-module-cups >= 1.9.74-alt2

%description -n python3-module-%name
The plugin adds the "Mark Job" context menu item. By invoking this action
a user can enter the desired job metadata and print it along with the job.

%description -n python3-module-%name -l ru_RU.UTF-8
Этот плагин добавляет операцию "Маркировка задания" по которой пользователь
может ввессти желаемые метаданные, которые будет напечатаны вместе
с документом.

%prep
%setup -n fonarik-%version

%build
python3 setup.py build

%install
python3 setup.py install \
    --root=%buildroot \
    --install-lib=%python3_sitelibdir_noarch

%files -n python3-module-%name
%python3_sitelibdir_noarch/system_config_printer_fonarik
%python3_sitelibdir_noarch/system_config_printer_fonarik-*.egg-info

%changelog
* Tue Jun 22 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt4
- Requires system-config-printer instead of system-config-printer-lib.

* Mon Jun 21 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Fix: Package the python module in the
  python3-module-system-config-printer-fonarik.

* Mon Jun 21 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Require python3(cups) >= 1.9.74-alt2.
- Use the job user name as is if getpwnam() raises KeyError.
- Fixed errors.

* Mon Jun 21 2021 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Using "fonarik" code moved system-config-printer v1.5.11-alt10.
- Initial release for Sisyphus.
