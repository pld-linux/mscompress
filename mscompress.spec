Summary:	MS compress/expand-compatible (de)compressor
Summary(pl.UTF-8):	(De)kompresor zgodny z MS compress/expand
Name:		mscompress
Version:	0.3
Release:	3
License:	GPL
Group:		Applications/Archiving
Source0:	ftp://ftp.penguin.cz/pub/users/mhi/mscompress/%{name}-%{version}.tar.bz2
# Source0-md5:	e85fe2fb0df95a7a921ecd867933ff89
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%description -l pl.UTF-8
Program kompresujący i dekompresujący zgodny z compress.exe/expand.exe
Microsoftu.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub .
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mscompress msexpand $RPM_BUILD_ROOT%{_bindir}
install mscompress.1 msexpand.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO format.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
