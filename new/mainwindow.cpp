#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_Act_Update_triggered()
{

}

void MainWindow::on_Act_Open_triggered()
{

}


void MainWindow::on_puB_method_clicked()
{

}

void MainWindow::on_puB_method_filter_clicked()
{

}
